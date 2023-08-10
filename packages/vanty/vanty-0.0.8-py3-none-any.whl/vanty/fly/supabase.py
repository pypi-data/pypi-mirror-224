import os
import subprocess
import random
import string
import json
import requests
import re
from getpass import getpass
from typing import Dict, Any, Optional
from jwcrypto import jwk, jwt
import secrets

# Create cli program helper and options
class CLIInfo:
    def __init__(self):
        self.username = ""
        self.default_region = ""
        self.organization = ""
        self.jwt_tokens = {"anon_token": "", "service_token": "", "JWT_SECRET": ""}
        self.pg_meta = {"ipv6": ""}
        self.pg_rest = {"ipv6": ""}
        self.pg_auth = {"ipv6": ""}
        self.database = {"ipv6": ""}
        self.kong = {"ipv6": "", "public_url": ""}
        self.studio = {"ipv6": "", "public_url": ""}

global_info = CLIInfo()


# You are entering function forest
# Proceed with caution

def get_default_fly_args(args: CLIInfo) -> list:
    args_array = ["--force-machines", "--auto-confirm"]
    if args.organization:
        args_array.extend(["--org", args.organization])
    if args.default_region:
        args_array.extend(["--region", args.default_region])
    return args_array

def user_auth(options: Dict[str, Any], spinner: Any) -> str:
    username = whoami()
    if not username:
        fly_login()
        username = whoami()
    elif not options.get('yes'):
        spinner.stop()
        resp = input(f"You are logged into Fly.io as: {username}. Do you want to continue? (y/n): ")
        if resp.lower() != 'y':
            fly_login()
            username = whoami()
    return username

def fly_login():
    subprocess.run(["fly", "auth", "login"])

def whoami() -> str:
    result = subprocess.run(["fly", "auth", "whoami"], stdout=subprocess.PIPE)
    return result.stdout.decode().strip()

def chose_default_regions() -> str:
    regions = subprocess.run(["fly", "platform", "regions"], stdout=subprocess.PIPE)
    regions = regions.stdout.decode().split("\n")[1:]
    options = [{"city": info.split("\t")[1], "code": info.split("\t")[0].strip()} for info in regions if info]
    for i, option in enumerate(options):
        print(f"{i+1}. {option['city']} {option['code']}")
    choice = int(input("Select a default region: ")) - 1
    return options[choice]['code']

# Fly io specific functions
# Deploying postgres-meta
def deploy_pg_meta(user_default_args: list):
    meta_name = None
    if not options.get('yes'):
        meta_name = input("Enter a name for your postgres metadata instance, or leave blank for a generated one: ")
    print("Deploying metadata...")
    name_commands = ["--name", meta_name] if meta_name else ["--generate-name"]
    update_pg_meta_docker_file_pg_host("../apps/pg-meta/Dockerfile", global_info.database['ipv6'])
    meta_launch_command_array = ["launch"] + launch_default_args + user_default_args + name_commands
    global_info.pg_meta['ipv6'] = fly_launch_deploy_internal_ipv6(meta_launch_command_array, "../apps/pg-meta")
    print("Metadata deployed")

def update_pg_meta_docker_file_pg_host(file_path: str, new_internal_address: str):
    with open(file_path, 'r') as file:
        data = file.read()
    data = data.replace('PG_META_DB_HOST=".*"', f'PG_META_DB_HOST="{new_internal_address}"')
    with open(file_path, 'w') as file:
        file.write(data)

def fly_launch_deploy_internal_ipv6(launch_command_array: list, path: str, secrets: Optional[Dict[str, Any]] = None) -> str:
    subprocess.run(["fly"] + launch_command_array, cwd=path)
    allocate_private_ipv6(path)
    if secrets:
        set_fly_secrets(secrets, path)
    fly_deploy(path)
    return get_internal_ipv6_address(path)

def allocate_private_ipv6(path: str):
    subprocess.run(["fly", "ips", "allocate-v6", "--private"], cwd=path)

def set_fly_secrets(secrets: Dict[str, Any], path: str):
    args = [f"{key}={value}" for key, value in secrets.items()]
    subprocess.run(["fly", "secrets", "set"] + args, cwd=path)

def fly_deploy(path: str):
    subprocess.run(["fly", "deploy"], cwd=path)

def get_internal_ipv6_address(proj_path: str) -> str:
    result = subprocess.run(["fly", "ssh", "console", "--command", "cat etc/hosts"], cwd=proj_path, stdout=subprocess.PIPE)
    match = re.search(r"([0-9a-fA-F:]+)\s+fly-local-6pn", result.stdout.decode())
    return match.group(1) if match else ""

def fly_auth():
    print("Checking fly cli authorization...")
    global_info.username = user_auth(options, None)
    print(f"Deploying to fly.io as: {global_info.username}")

def fly_set_default_region():
    global_info.default_region = options.get('region') or chose_default_regions()
    print(f"Deploying to region: {global_info.default_region}")

def fly_set_default_org():
    global_info.organization = options.get('org') or "personal"
    print(f"Deploying to organization: {global_info.organization}")

def fly_deploy_and_prepare_db(default_args: list):
    if not options.get('dbUrl'):
        print("Deploying your database...")
        global_info.database['ipv6'] = deploy_database(default_args)
        print("You successfully deployed your database!")

# Rest of the functions are similar to the ones above and can be converted in the same way

def generate_supa_jwts():
    signing_key = jwk.JWK.generate(kty='oct', size=256)
    anon_claims = {"role": "anon", "iss": "supabase"}
    service_claims = {"role": "service_role", "iss": "supabase"}
    global_info.jwt_tokens['anon_token'] = jwt.JWT(header={"alg": "HS256"}, claims=anon_claims).serialize(signing_key)
    global_info.jwt_tokens['service_token'] = jwt.JWT(header={"alg": "HS256"}, claims=service_claims).serialize(signing_key)
    global_info.jwt_tokens['JWT_SECRET'] = signing_key.export()

launch_default_args = ["--no-deploy", "--copy-config", "--reuse-app", "--force-machines"]

def main():
    # check if fly cli is authenticated
    fly_auth()

    # generate service and anon tokens
    generate_supa_jwts()

    # chose default region if not passed in
    fly_set_default_region()

    # set default org if passed in
    fly_set_default_org()

    # turn our info object into default fly args
    default_args = get_default_fly_args(global_info)

    # deploy database
    fly_deploy_and_prepare_db(default_args)

    # deploy api
    deploy_pg_meta(default_args)

    # deploy postGREST
    deploy_pg_rest(default_args)

    deploy_auth(default_args)

    deploy_clean_up()

    deploy_kong(default_args)

    api_gateway_test()

    deploy_studio(default_args)

    studio_test()

if __name__ == "__main__":
    main()

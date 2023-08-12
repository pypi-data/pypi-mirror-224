import os
from dotenv import load_dotenv

from locker import Locker


load_dotenv()
access_key = os.getenv("ACCESS_KEY_TEST")
headers = {
    "cf-access-client-id": os.getenv("CF_ACCESS_CLIENT_ID"),
    "cf-access-client-secret": os.getenv("CF_ACCESS_CLIENT_SECRET")
}

locker = Locker(access_key=access_key, options={"headers": headers})


# List environments
environments = locker.list_environments()
for environment in environments:
    print(environment.name, environment.external_url, environment.description)


# Get an environment by name
environment = locker.get_environment("staging")
print(environment.name, environment.external_url, environment.description)


# Update an environment by name
environment = locker.modify_environment(name="staging", external_url="staging.demo.environment")
print(environment.name, environment.external_url, environment.description)


# Create new environment
new_environment = locker.create_environment(name="Production", external_url="prod.demo.environment")
print(new_environment.name, new_environment.external_url, new_environment.description)

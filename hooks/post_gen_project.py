"""
Setup envs for dev environment
"""

import secrets
import shutil
import os


def get_random_string():
    return secrets.token_urlsafe(16)


def set_key_random(file_path, key):
    secret = get_random_string()

    with open(file_path, 'r+') as config_file:
        file_contents = config_file.read().replace(key, secret, 1)
        config_file.seek(0)
        config_file.write(file_contents)
        config_file.truncate()


def copy_dev_env():
    env_template = '.env.template'
    env_file = '.env'
    shutil.copyfile(env_template, env_file)
    set_key_random(env_file, '__DJANGO_SECRET_KEY__')
    set_key_random(env_file, '__POSTGRES_PASSWORD___')


def create_docs():
    docs_dir = 'docs'
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    readme_content = """# My Project

This is a sample README file for the project.
"""
    with open(os.path.join(docs_dir, 'README.md'), 'w') as readme_file:
        readme_file.write(readme_content)

    requirements_content = """# Documentation Requirements

List of documentation requirements goes here.
"""
    with open(os.path.join(docs_dir, 'requirements.txt'), 'w') as requirements_file:
        requirements_file.write(requirements_content)

def pre_gen_script():

    include_docs = input("Do you want to include documentation? (yes/no): ").lower().strip()

    while include_docs not in ['yes', 'no']:
        include_docs = input("Please enter 'yes' or 'no': ").lower().strip()

    if include_docs == 'yes':
        create_docs()
    elif include_docs == 'no':
        print("Documentation will not be included.")




def main():
    copy_dev_env()
    create_docs()
    


if __name__ == "__main__":
    main()

# pre_gen_script.py

import os

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

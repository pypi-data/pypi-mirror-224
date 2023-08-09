import pytest
import subprocess


def run_command(command):
    try:
        # Use subprocess.run to run the command and capture the output
        completed_process = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)

        # Print the standard output and standard error (if any)
        print("Standard Output:")
        print(completed_process.stdout)

        if completed_process.stderr:
            print("Standard Error:")
            print(completed_process.stderr)

        # Check the return code to see if the command was successful (return code 0)
        if completed_process.returncode == 0:
            print("Command executed successfully.")
        else:
            print(f"Command failed with return code {completed_process.returncode}.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")


if __name__ == "__main__":
    pytest.main(["tests"])
    run_command("cd docs")
    run_command("make html")

from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
    long_description = fh.read()

import os

version_ns = {}
with open(os.path.join("liveramp_automation", "__version__.py")) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

setup(
    name='liveramp_automation',
    version=version,
    author='Jasmine Qian',
    author_email='jasmine.qian@liveramp.com',
    description="This is the base liveramp_automation_framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LiveRamp/liveramp-automation",
    packages=find_packages(),
    install_requires=[
        'pytest',
        'pytest-bdd',
        'pytest-playwright',
        'allure-pytest-bdd',
        'allure-python-commons',
        'google',
        'google-api-core',
        'google-auth',
        'google-cloud-bigquery',
        'google-cloud-core',
        'google-cloud-storage',
        'google-crc32c',
        'google-resumable-media',
        'googleapis-common-protos',
        'PyYAML',
        'pytest-json-report',
        'pytest-json',
        'pytest-xdist',
        'requests',
        'selenium==4.8.3',
        'pytest-bdd==6.1.1',
        'PyYAML==6.0',
        'webdriver-manager==3.8.6',
        'retrying==1.3.4',
    ],
)

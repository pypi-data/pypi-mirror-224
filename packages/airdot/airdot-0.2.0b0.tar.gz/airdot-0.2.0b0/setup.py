from setuptools import find_packages, setup
import pathlib
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRES_PYTHON = ">=3.7.0"
REQUIRED = [
    "black==22.6.0",
    "pytest==7.1.2",
    "PyYAML==5.4.1",
    "google-api-python-client==2.78.0",
    "google-cloud-core==2.3.2",
    "google-cloud-storage==2.7.0",
    "google-auth",
    "zstd==1.5.2.6",
    "boto==2.49.0",
    "botocore==1.29.127",
    "boto3==1.26",
    "docker==6.1.2",
    "redis==4.5.5",
    "seldon-core==1.16",
    "pydantic==1.10.8",
    "kubernetes==26.1.0"
]
DEV_REQUIRED = [
    "black==22.6.0",
    "pytest==7.1.2",
    "PyYAML==5.4.1",
    "google-api-python-client==2.78.0",
    "google-cloud-core==2.3.2",
    "google-cloud-storage==2.7.0",
    "google-auth",
    "zstd==1.5.2.6",
    "boto==2.49.0",
    "botocore==1.29.127",
    "boto3==1.26",
    "docker==6.1.2",
    "redis==4.5.5",
    "seldon-core==1.16",
    "pydantic==1.10.8",
    "kubernetes==26.1.0"
]

def version(rel_path):
    file = open(rel_path, 'r').read()
    for line in file.splitlines():
        if line.startswith("VERSION"):
            return line.split("=")[1]
    raise RuntimeError("Unable to find version string.")

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
if os.path.exists("airdot/version.py"):
    VERSION = version("airdot/version.py")
else:
    raise RuntimeError('version file not found')

setup(
    name="airdot",
    url="https://github.com/airdot-io/airdot-Deploy/",
    author="airdot-io",
    author_email="abhhinav035991@gmail.com",
    packages=find_packages(),
    version=VERSION,
    description="A code base for deploying python functions",
    long_description=long_description,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
)

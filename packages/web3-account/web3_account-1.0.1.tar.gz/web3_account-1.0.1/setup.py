from io import open
from setuptools import setup

version = '1.0.1'

with open("README.md", encoding='utf-8') as file:
    long_descr = file.read()

setup(
    name="web3_account",
    version=version,

    author="lang123",
    author_email="dima.lang3103@gmail.com",

    url="https://github.com/langeth123/Web3Account",
    download_url="https://github.com/langeth123/Web3Account/archive/v{}.zip".format(version),

    packages=["web3_account"],
    install_requires=["web3", "requests", "loguru"],
    long_description=long_descr,
    license="Apache License, Version 2.0, see LICENSE file",
    description="The simplest way to use Web3 features",
    long_description_content_type="text/markdown"


)
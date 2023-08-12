from io import open
from setuptools import setup

version = '1.0'

setup(
    name="web3_account",
    version=version,

    author="lang123",
    author_email="dima.lang3103@gmail.com",

    url="https://github.com/langeth123/Web3Account",
    download_url="https://github.com/langeth123/Web3Account/archive/v{}.zip".format(version),

    packages=["web3_account"],
    install_requires=["web3", "requests", "loguru"]


)
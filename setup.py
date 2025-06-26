from setuptools import setup, find_packages

with open("version.txt") as f:
    version = f.read().strip()

setup(
    name="libversion",
    version=version,
    packages=find_packages(),
    install_requires=[
        "toml >= 0.10.2"
    ],
)

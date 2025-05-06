from setuptools import setup, find_packages

setup(
    name="libversion",
    version="0.0.3",
    packages=find_packages(),
    install_requires=[
        "toml >= 0.10.2"
    ],
)

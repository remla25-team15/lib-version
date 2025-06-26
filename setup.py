from setuptools import find_packages, setup


def get_version():
    import os

    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, "libversion/version_self.py")) as f:
        return f.read().strip()


setup(
    name="libversion",
    version=get_version(),
    packages=find_packages(),
    install_requires=["toml >= 0.10.2"],
)

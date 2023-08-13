from setuptools import setup

with open("requirements.txt") as requirements_file:
    require = requirements_file.read()
    requirements = require.split()

setup(
    name="sgeom",
    version="0.1",
    description="A package handling geometries.",
    author="Juncheng E, Mats Fangohr",
    author_email="juncheng.e@xfel.eu",
    url="https://github.com/JunCEEE/sgeom",
    packages=["sgeom"],  # This should be a list of your package's submodules
    install_requires=requirements,  # List your package dependencies here
)

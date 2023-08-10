from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="OpenHashDB",
    version="0.0.1",
    description="Official Python Package to easily integrate the OpenHashDB API to your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Paul Harrer",
    author_email="support@openhashdb.com",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    project_urls={
        "GitHub": "https://github.com/PaulHarrer/openhashdb-python",
    },
)

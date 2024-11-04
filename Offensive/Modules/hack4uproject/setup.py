from setuptools import setup, find_packages

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()


setup(
    name = "hack4upolsiv",
    version = "0.1.2",
    packages = find_packages(),
    install_requires = [],
    author = "Polsiv",
    description = "Library for hack4u courses",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://hack4u.io",
)

 
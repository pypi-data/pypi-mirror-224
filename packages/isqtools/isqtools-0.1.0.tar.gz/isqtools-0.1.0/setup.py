# This code is part of isQ.
# (C) Copyright ArcLight Quantum 2023.
# This code is licensed under the MIT License.

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

requirements = [
    "autograd",
]

setup(
    name="isqtools",
    version="0.1.0",
    description="python tools for isQ",
    platforms="python 3.8+",
    python_requires=">=3.8",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yusheng Yang",
    author_email="yangys@arclightquantum.com",
    license="MIT",
    packages=find_packages(where="."),
    package_data={"": ["*.txt"]},
    install_requires=requirements,
)

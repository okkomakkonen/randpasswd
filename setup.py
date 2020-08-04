"""
Setup script for randpasswd
"""
import setuptools  # type: ignore

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="randpasswd",
    version="1.0",
    description="Random passphrase generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    package_dir={"randpasswd": "randpasswd"},
    package_data={"randpasswd": ["wordlist.txt"]},
    python_requires=">=3.6",
    entry_points={"console_scripts": ["randpasswd=randpasswd.randpasswd:main"]},
)

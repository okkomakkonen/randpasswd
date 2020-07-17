"""
Setup script for randpasswd
"""
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="randpasswd",
    version="0.0.1",
    description="Random passphrase generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)

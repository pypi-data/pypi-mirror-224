"""
Package setup script for microservice_shared.
"""

from io import open

from setuptools import find_packages, setup

setup(
    name="microservice_shared",
    version="0.2.0",
    description="A common package for Django REST framework",
    author="Manikandan",
    author_email="manikandan.findmyjobz@gmail.com",
    packages=find_packages(),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "Django",
        "djangorestframework",
        # Add any other dependencies your package requires
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)

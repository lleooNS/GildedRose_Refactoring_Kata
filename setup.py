from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="GildedRose_Refactoring_Kata",
    version="0.0.1",
    author="Leonardo Nascimento dos Santos",
    description="Refactor the project: The Gilded Rose Kata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license_files='license.txt',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Local Environment",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "License :: Other/Proprietary License",
    ],
    python_requires="==3.8.3",
    install_requires=[
        "pip-chill==1.0.1",
        "texttest==4.0.9.1",
        "python-dotenv==0.19.2"
    ]
)

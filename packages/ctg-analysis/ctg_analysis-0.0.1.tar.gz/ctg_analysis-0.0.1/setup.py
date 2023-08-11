from setuptools import setup, find_packages

setup(
    name="ctg_analysis",
    version="0.0.1",
    author="Maxi Linares",
    author_email="maxi-linares@hotmail.com",
    description="Python library for the automatic cardiotocogram (CTG) analysis and interpretation",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mlinaresv/ctg_analysis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "matplotlib>=3.5.1",
        "BaselineRemoval>= 0.1.4",
        "numpy>=1.16.0",
        "scipy>=1.7.0",
        "pandas>=1.2.0"
    ],
)
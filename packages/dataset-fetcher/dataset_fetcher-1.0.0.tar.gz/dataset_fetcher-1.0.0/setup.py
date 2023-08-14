from setuptools import setup, find_packages
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # This is the name of the package
    name="dataset_fetcher",    

    # The initial release version               
    version="1.0.0",    

    # Full name of the author                    
    author="DATAISENOUGH",
    author_email='dataisenough@gmail.com',
    # Long description read from the the readme file                     
    description="A package for fetching datasets for Analytics purposes",
    # url='https://github.com/yourusername/
    long_description=long_description,      
    long_description_content_type="text/markdown",

    # List of all python modules to be installed
    packages=setuptools.find_packages(), 

    # Information to filter the project on PyPi website   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],   
    # Minimum version requirement of the package                                   
    python_requires='>=3.8',   

    # Name of the python package             
    py_modules=["DataFetcher"],     

    # Directory of the source code of the package        
    package_dir={'':'DataFetcher/src'},

    # Install other dependencies if any   
    install_requires=[
        'pandas',
        'requests',
        'tabulate',
    ],             
)
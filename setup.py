import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Read the requirements
with open("requirements.txt",encoding="utf8") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="edaSQL",  # This is the name of the package
    version="0.0.1.5",  # The initial release version
    author="Tamil Selvan A V",  # Full name of the author
    description="Exploratory Data Analytics tool for SQL",
    url="https://github.com/selva221724/edaSQL",
    license="MIT",
    include_package_data=True,
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Framework :: IPython",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Scientific/Engineering",
        "Environment :: Console"
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.6',  # Minimum version requirement of the package
    py_modules=["edaSQL"],  # Name of the python package
    package_dir={'': 'edaSQL/src'},  # Directory of the source code of the package
    install_requires=requirements  # Install other dependencies if any

)

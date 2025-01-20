from setuptools import setup, find_packages

# Open the README file to include a detailed long description for the package
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Topsis_Jeevetesh_102383041",  # Name of the package, ensuring uniqueness on PyPI
    version="1.0.1",  # Version number following semantic versioning
    author="Jeevetesh",  # Author name
    author_email="testcse02@gmail.com",  # Author's email address for contact
    url="https://github.com/Jeevetesh/Topsis_102383041",  # URL of the GitHub repository
    description="A Python package for TOPSIS implementation in multi-criteria decision analysis",  # Short description of the package
    long_description=long_description,  # Detailed description from the README file
    long_description_content_type="text/markdown",  # Format of the long description
    packages=find_packages(),  # Automatically find all packages in the project
    classifiers=[
        "Programming Language :: Python :: 3",  # Indicates support for Python 3
        "License :: OSI Approved :: MIT License",  # Specifies the license type
        "Operating System :: OS Independent",  # Compatible with all operating systems
    ],
    install_requires=["pandas>=1.0.0", "numpy>=1.18.0"],  # Dependencies required for the package
    entry_points={
        "console_scripts": [
            # Command-line entry point for the package
            "Topsis_Jeevetesh_102383041 = Topsis_Jeevetesh_102383041.topsis:main"
        ],
    },
)

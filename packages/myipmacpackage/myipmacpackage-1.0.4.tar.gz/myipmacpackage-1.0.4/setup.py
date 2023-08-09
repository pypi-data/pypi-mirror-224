from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.run(["myipmac-fetcher"])  # Run the script after installation

setup(
    name="myipmacpackage",
    version="1.0.4",
    description="Fetch and store IP and MAC addresses in a database",
    author="Muneer",
    author_email="Muneer.moosa@electrifex.com",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        "install": PostInstallCommand,
    },
    entry_points={
        "console_scripts": [
            "myipmac-fetcher=myipmac.fetcher:main"  # Automatically run fetcher.py
        ]
    }
)

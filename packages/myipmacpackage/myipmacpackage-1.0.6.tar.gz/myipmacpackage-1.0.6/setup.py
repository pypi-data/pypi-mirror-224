from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        script_path = os.path.join(self.install_scripts, "post_install.py")
        subprocess.run(["python3", script_path])  # Run the script after installation

setup(
    name="myipmacpackage",
    version="1.0.6",
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
            "run_fetcher = myipmac.fetcher:main"
        ]
    }
)

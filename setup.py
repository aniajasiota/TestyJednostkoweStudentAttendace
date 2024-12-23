import os
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

version = os.getenv(
    "VERSION",
    "0.0.0",  
)

setup(
    name="project369367447",
    version=version,
    author="xanniaqx",
    author_email="anna.jasiota@edu.uekat.pl",
    description="Attendance management system for university",
    url="https://github.com/aniajasiota/TestyJednostkoweStudentAttendace.git",
    packages=find_packages(
        include=["src.*"],
        exclude=["tests.*"],
    ),
     install_requires=required_packages,  # requirements from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.13",
    entry_points={
        "console_scripts": [
            "menageStudents=src.main:main",  # script when someone uses menageStudents in console he can run this app
        ]
    },
)

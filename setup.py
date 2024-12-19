import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="project369367447",
    version=version,
    author="xanniaqx",
    author_email="anna.jasiota@edu.uekat.pl",
    description="Attendance management system for university",
    long_description_content_type="text/markdown",
    url="https://github.com/aniajasiota/TestyJednostkoweStudentAttendace.git",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["TestyJednostkoweStudentAttendance=main:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
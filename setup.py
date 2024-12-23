import os
from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

Versions = os.getenv('PACKAGE_VERSION', '0.0.0')


setup(
    name='project369367447',
    version=Versions,
    description='A sample Python function package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Anna Jasiota',
    author_email='anna.jasiota@edu.uekat.pl',
    url='https://github.com/aniajasiota/TestyJednostkoweStudentAttendace.git',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.9',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
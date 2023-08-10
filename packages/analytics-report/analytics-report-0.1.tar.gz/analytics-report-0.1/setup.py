from setuptools import setup, find_packages

setup(
    name='analytics-report',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'google-analytics-data'
    ],
    author='Your Name',
    description='A library to run reports on Google Analytics',
)

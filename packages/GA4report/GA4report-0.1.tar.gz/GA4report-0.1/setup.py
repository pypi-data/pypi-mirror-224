from setuptools import setup, find_packages

setup(
    name='GA4report',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'google-analytics-data'
    ],
    author='Sang',
    description='A library to run reports on Google Analytics',
)

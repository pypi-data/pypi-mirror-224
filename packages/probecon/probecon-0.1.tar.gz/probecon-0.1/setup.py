from setuptools import setup, find_packages

setup(
    name='probecon',
    version='0.1',
    description='A Python package for subdomain enumeration',
    author='Probe',
    author_email='whoami_anoint@bugcrowdninja.com',
    url='https://github.com/whoami-anoint/Probe',
    packages=['probecon'],
    install_requires=[
        'amass',       # Add other dependencies like 'amass', 'subfinder', 'anubis' if needed
        'subfinder',
        'anubis',
        'httpx',
    ],
)

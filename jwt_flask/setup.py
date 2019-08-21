"""
JWT Example App
"""

from setuptools import setup, find_packages

setup(
    name='jwt_flask',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'Flask',
        'flask-jwt-extended'
    ]
)

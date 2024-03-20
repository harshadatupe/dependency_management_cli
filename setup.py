from setuptools import setup, find_packages

setup(
    name='deps_manager',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'deps_manager = deps_manager.main:main',
        ],
    },
)
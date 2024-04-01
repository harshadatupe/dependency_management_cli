from setuptools import setup, find_packages

setup(
    name='deps-manager',
    version='1.0.7',
    author="Harshada Tupe",
    author_email="harshadatupe8@gmail.com",
    license="MIT",
    packages=find_packages(),
    classifiers=["Python 3.9", "Cross Platform"],
    python_requires='>=3.5',
    entry_points={
        'console_scripts': [
            'deps-manager = deps_manager.main:main',
        ],
    },
)
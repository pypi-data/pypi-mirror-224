from setuptools import find_packages, setup

setup(
    name='pages',
    packages=find_packages(include=['pages']),
    version='0.3.4',
    description='Encrypted dicts',
    author='J.DeKeyrel',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
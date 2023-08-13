from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='vtils',
    packages=find_packages(include=['vtils']),
    version='0.1.1',
    description='Vtils Python Library',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author='Venkateswara Rao Thota',
    license='MIT',
    install_requires=['PyCryptodome','boto3'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)

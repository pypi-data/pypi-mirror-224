from setuptools import setup, find_packages

setup(
    name='shining-brain',
    version='0.1',
    description='Making decisions by analyzing data',
    author='Evan Knox Thomas',
    author_email='evanknoxthomas@gmail.com',
    packages=find_packages(),
    install_requires=['pandas', 'sqlalchemy', 'PyYAML'],
)

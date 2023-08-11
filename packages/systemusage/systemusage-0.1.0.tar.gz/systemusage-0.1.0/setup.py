from setuptools import setup, find_packages

setup(
    name='systemusage',
    version='0.1.0',
    description='A real-time system resource monitoring utility package',
    author='Pytech Academy',
    author_email='pytechacademy@gmail.com',
    url='https://github.com/PytechAcademy/PackagePublishing',
    packages=find_packages(),
    install_requires=[
        'psutil'
    ],
)

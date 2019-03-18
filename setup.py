from setuptools import setup, find_packages

setup(
    name='my-python-package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Mlungiseleli Notshokovu python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/mlungiseleli-notshokovu/mypackage',
    author='<Mlungiseleli Notshokovu>',
    author_email='<mlungiselelinotshokovu@gmail.com>'
)
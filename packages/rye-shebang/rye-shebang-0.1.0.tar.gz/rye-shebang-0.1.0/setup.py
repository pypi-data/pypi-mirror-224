#!/usr/bin/env python


import pathlib

from setuptools import setup

with open(pathlib.Path(__file__).parent / 'README.md', encoding='utf-8') as f:
    readme = f.read()

if pathlib.Path('/bin/bash').exists():
    scripts = ['bash/rye-shebang']
else:
    scripts = ['py/rye-shebang']

setup(
    name='rye-shebang',
    version='0.1.0',
    url='https://github.com/Tacha-S/rye-shebang',
    author='Tatsuro Sakaguchi',
    author_email='tacchan.mello.ioiq@gmail.com',
    description='rye-shebang allows you to put scripts in your path that run in a rye environment.',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=[],
    install_requires=[],
    scripts=scripts,
    data_files=[('py', ['py/rye-shebang']), ('bash', ['bash/rye-shebang'])],
)

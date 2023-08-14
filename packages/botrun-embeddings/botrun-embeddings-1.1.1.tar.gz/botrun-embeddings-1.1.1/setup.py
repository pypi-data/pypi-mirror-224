
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="botrun-embeddings",
    version="1.1.1",
    packages=find_packages(),
    py_modules=['botrun_embeddings'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'botrun_embeddings = botrun_embeddings:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)

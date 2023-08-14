
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="botrun-pdf-qa",
    version="1.0.0",
    packages=find_packages(),
    py_modules=['botrun_pdf_qa'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'botrun_pdf_qa = botrun_pdf_qa:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)

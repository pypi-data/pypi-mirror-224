
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name="botrun-pdf-to-text",
    version="1.1.0",
    packages=find_packages(),
    py_modules=['botrun_pdf_to_text'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'botrun_pdf_to_text = botrun_pdf_to_text:main',
        ],
    },
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',)

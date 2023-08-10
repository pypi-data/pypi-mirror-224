# setup.py

from setuptools import setup, find_packages

setup(
    name='roman-nepali-translator',
    version='0.1.1',
    packages=find_packages(),
    author='Milan Yadav',
    author_email='ymilan.projects@gmail.com',
    description='A package for translating Romanized English to Unicode Nepali',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MILANydv/nepali_translator_package.git',
    install_requires=[
        # No additional dependencies needed
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

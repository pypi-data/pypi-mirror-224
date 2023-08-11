from setuptools import setup, find_packages

setup(
    name='scrapy_selenium_tmt',
    version='0.0.9',
    description='Scrapy with selenium',
    auther='ThunderMindTech',
    packages=find_packages('requirements/requiremets.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)
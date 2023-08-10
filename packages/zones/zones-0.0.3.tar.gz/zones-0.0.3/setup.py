import setuptools
from setuptools import setup, find_packages

setup(
    name='zones',
    version='0.0.3',
    author="Noel M Nguemechieu",
    author_email="nguemechieu@live.com",
    description="AI powered trading software for MetaTrader",
    long_description_content_type="text/x-rst",
    keywords=['run', 'open', 'trade'],
    url="https://github.com/nguemechieu/zones",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    install_requires=
        'requirements.txt',
    entry_points={
        'console_scripts': [
            'zones = zones.zones:main',
        ],

    },
    zip_safe=False,

)

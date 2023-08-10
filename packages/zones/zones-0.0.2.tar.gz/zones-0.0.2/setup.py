import setuptools

setuptools.setup(

    name="zones",
    version="0.0.2",
    author="Noel M Nguemechieu",
    author_email="nguemechieu@live.com",
    description="AI powered trading software for MetaTrader",
    long_description_content_type="text/x-rst",
    keywords=['run', 'open', 'trade'],
    url="https://github.com/nguemechieu/zones",
    include_package_data=True,
    package_dir={'ZONES': 'src'},
    packages=['ZONES'],
    license='License :: MIT License',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry"
    ],
    python_requires='>=3.11'
)

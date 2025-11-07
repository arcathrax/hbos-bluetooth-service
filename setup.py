
from setuptools import setup, find_packages

setup(
    name="hbos-bluetooth-service",
    version="0.1.0",
    description="HBOS Bluetooth Service",
    long_description="A service for managing Bluetooth devices and connections on HBOS.",
    author="HBOS",
    author_email="support@hbos.com",
    license="MIT",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "hbos-bluetooth = main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

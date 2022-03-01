from setuptools import setup, find_packages

setup(
    name='rcplant',
    version='1.1.2',
    url='',
    license='',
    author='Mohammadreza Rostam, Rongxuan Du',
    author_email='reza.rostam@mech.ubc.ca',
    description='Recycling Plant Simulator',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering"
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={'rcplant/data': ['rcplant/data/*.xlsx']},
    python_requires='>=3.8',
    install_requires=["pandas>=1.3.4", "openpyxl>=3.0.9", "numpy>=1.21.5"]
)

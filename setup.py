from setuptools import setup, find_packages

setup(
    name='rcplant',
    version='0.9.50',
    url='',
    license='',
    author='Mohammadreza Rostam, Rongxuan Du',
    author_email='reza.rostam@mech.ubc.ca',
    description='Recycling Plant Simulator',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering"
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={'rcplant/data': ['rcplant/data/*.xlsx']},
    python_requires='>=3.8',
    install_requires=["matplotlib>=3.3.3", "pandas>=1.3.4", "openpyxl>=3.0.9", "numpy>=1.21.5"]
)

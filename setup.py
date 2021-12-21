from setuptools import setup, find_packages

setup(
    name='rcplant',
    version='0.3.0',
    url='',
    license='',
    author='Mohammadreza Rostam, Rongxuan Du',
    author_email='reza.rostam@mech.ubc.ca, Rongxuan Du',
    description='Recycling Plant Simulator',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: Free for non-commercial use",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Multimedia :: Sound/Audio :: Speech"
    ],
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=["matplotlib>=3.3.3", "pandas>=1.3.4", "tabulate>=0.8.9", "openpyxl>=3.0.9"]
)

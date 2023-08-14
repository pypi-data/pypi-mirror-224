from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Programming Language :: Python :: 3 :: Only",  # Specify Python 3 only
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name='gps2gtfs',
    packages=find_packages(),
    version='0.0.2-rc2',
    description='Extracting travel time information from Bus GPS raw data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/aaivu/gps2gtfs',
    keywords=['gtfs', 'GPS', 'travel time', 'bus travel time prediction'],
    author='AAIVU',
    author_email='helloaaivu@gmail.com',
    license='MIT',
    classifiers=classifiers,
    python_requires=">=3.6",
    install_requires=['pandas', 'geopandas', 'numpy']
)

from setuptools import setup, find_packages
from setuptools import  find_namespace_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='anticp2',
    version='1.0',
    description='A tool to predict anti-cancerous peptides',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE.txt',),
    url='https://github.com/raghavagps/anticp2', 
    packages=find_namespace_packages(where="src"),
    package_dir={'':'src'},
    package_data={'anticp2.model':['*']},
    entry_points={ 'console_scripts' : ['anticp2 = anticp2.python_scripts.anticp2:main']},
    include_package_data=True,
    python_requires='>=3.3, <=3.7',
    install_requires=[
        'numpy', 'pandas', 'sklearn==0.21.3', 'pickle-mixin' # Add any Python dependencies here
    ]
)
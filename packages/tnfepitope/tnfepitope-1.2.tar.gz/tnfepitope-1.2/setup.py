from setuptools import setup, find_packages
from setuptools import  find_namespace_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='tnfepitope',
    version='1.2',
    description='A webserver for prediction of TNF inducing epitopes' ,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE.txt',),
    url='https://gitlab.com/raghavalab/tnfepitope', 
    packages=find_namespace_packages(where="src"),
    package_dir={'':'src'},
    package_data={'tnfepitope.blast_binaries':['**/*'],
    'tnfepitope.blast_db':['**/*'],
    'tnfepitope.model':['*']},
    entry_points={ 'console_scripts' : ['tnfepitope = tnfepitope.python_scripts.tnfepitope:main']},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'numpy', 'pandas', 'scikit-learn', 'argparse' # Add any Python dependencies here
    ],
)
    


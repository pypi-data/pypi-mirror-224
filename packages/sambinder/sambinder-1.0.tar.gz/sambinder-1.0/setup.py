from setuptools import setup, find_packages
from setuptools import  find_namespace_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='sambinder',
    version='1.0',
    description='A tool for predicting S-adenosyl-L-methionine binding sites',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE',),
    url='https://github.com/raghavagps/sambinder', 
    packages=find_namespace_packages(where="src"),
    package_dir={'':'src'},
    package_data={'sambinder.code':['*'], 
    'sambinder':['*'],
},
    entry_points={ 'console_scripts' : ['sambinder = sambinder.sambinder:main']},
    include_package_data=True,
    python_requires='>=3.5, <=3.7',
    install_requires=[
        'numpy', 'pandas',  'argparse', 'joblib', 'scikit-learn==0.21.2' # Add any Python dependencies here
    ]
)

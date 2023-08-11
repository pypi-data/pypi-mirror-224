from setuptools import setup, find_packages
from setuptools import find_namespace_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='fluspred',
    version='0.8',
    description='A bioinformatic-ware to predict the zoonotic host tropism of Influenza A virus.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files=('LICENSE.txt',),
    url='https://github.com/raghavagps/fluspred',
    packages=find_namespace_packages(where="src"),
    package_dir={'': 'src'},
    package_data={
        'fluspred.Models': ['*']
    }, 
    entry_points={'console_scripts': ['fluspred = fluspred.python_scripts.maintain:main']},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'numpy==1.23.5', 'pandas==1.2.3', 'scikit-learn==1.0.2'
    ]
)

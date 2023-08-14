from setuptools import find_packages, setup

setup(packages=find_packages())

# Build package:
#   delete dist folder, coziepy.egg-info folder
#   python -m build

# Upload package to pypi:
#   py -m twine upload --repository testpypi dist/*    
#   py -m twine upload --repository pypi dist/*                   
from setuptools import setup, find_packages

setup(
    name='KunWang_ISAT',
    version='1.1',
    author='BeanBUN',
    author_email='1224273829@qq.com',
    install_requires=[
        'numpy',
        'shapely',
        'pandas',
        'geopandas',
    ],
    packages=find_packages()
)
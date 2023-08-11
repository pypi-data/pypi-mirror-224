from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='PyGeom3D',
    version='0.0.1',
    description='Useful tools to work Geometries in Python(beta)',
    long_description=README + '\n\n' + HISTORY,

    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    author='Rohit Jain',
    author_email='rohit.jain058@gmail.com',
    keywords=['Geometry', 'Python', 'Polygon', 'Plane', 'Line','3D'],
    url='https://github.com/jain-roh/Geom3D',
    download_url='https://pypi.org/project/PyGeom3D/'
)

install_requires = [
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
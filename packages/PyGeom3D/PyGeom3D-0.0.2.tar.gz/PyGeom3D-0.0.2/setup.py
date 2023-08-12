from setuptools import setup, find_packages

from Cython.Build import cythonize
import os
with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()


EXCLUDE_FILES = [
    'PyGeom3D/__init__.py'
]

def get_ext_paths(root_dir, exclude_files):
    """get filepaths for compilation"""
    paths = []

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            if os.path.splitext(filename)[-1] == '.c':
                pass
            else:
                continue

            file_path = os.path.join(root, filename)
            if file_path in exclude_files:
                continue

            paths.append(file_path)
    return paths

setup_args = dict(
    name='PyGeom3D',
    version='0.0.2',
    description='Useful tools to work Geometries in Python(beta)',
    long_description=README + '\n\n' + HISTORY,
    
    long_description_content_type="text/markdown",
    license='MIT',
    packages= ['PyGeom3D'],
    author='Rohit Jain',
    author_email='rohit.jain058@gmail.com',
    keywords=['Geometry', 'Python', 'Polygon', 'Plane', 'Line','3D'],
    url='https://github.com/jain-roh/Geom3D',
    download_url='https://pypi.org/project/PyGeom3D/'
)



install_requires = [
]


if __name__ == '__main__':
    setup(**setup_args, 
    install_requires=install_requires,
    ext_modules=cythonize(
        get_ext_paths('PyGeom3D', EXCLUDE_FILES),
        compiler_directives={'language_level': 3}
    )
    )
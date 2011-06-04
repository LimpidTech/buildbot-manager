from setuptools import setup, find_packages
import os, sys

# The repository root directory
project_root = os.path.abspath(os.path.dirname(__file__))

# The projects which this project depends upon
dependancies = [
    'pyramid',
    'buildbot',
    'repoze.tm2>=1.0b1',
    'WebError',
    'pyramid_jinja2',
]

# Files that contain different metadata which is used for setting up the project
meta_files = {
    'README.md': None,
    'CHANGES.md': None,
    'setup/CLASSIFIERS.txt': None,
    'setup/ENTRY_POINTS.ini': None,
}

# Read each of our files and update their data, or set them to a blank string.
for filename in meta_files:
    try:
        current_file = open(os.path.join(project_root, filename))
        meta_files[filename] = current_file.read()
        current_file.close()

    except IOError:
        meta_files[filename] = ''

setup(name='bbmanager',
      version='0.0.1-prototype',
      description='Manage your buildbot server with a nice web interface.',
      long_description=meta_files['README.md'],
      classifiers=meta_files['setup/CLASSIFIERS.txt'].split("\n"),
      author='Brandon R. Stoner',
      author_email='monokrome@limpidtech.com',
      url='http://github.com/LimpidTech/buildbot-manager',
      keywords='web pylons pyramid buildbot',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=dependancies,
      test_suite='bbmanager.test',
      entry_points=meta_files['setup/ENTRY_POINTS.ini'],
      paster_plugins=['pyramid'],
)

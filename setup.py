from setuptools import setup

setup(name='trans',
      version='0.1',
      packages=['trans'],
      author='Sam',
      include_package_data=True,
      install_requires=[
        'requests'
      ],
      scripts=['bin/trans'],
      zip_safe=False)
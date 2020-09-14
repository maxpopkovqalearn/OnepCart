from setuptools import  setup, find_packages


setup(name='otus-qa-opencart-testing',
      version='1.0',
      author='Max Popkov',
      license='MIT',
      description='Tests for Opencart',
      url='https://github.com/maxpopkovqalearn/OnepCart',
      packages=find_packages(),
      install_requires=['pytest', 'selenium'],
      long_description=open('README.md').read(),
      zip_safe=False)
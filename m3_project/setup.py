from setuptools import setup, find_packages


setup(
      name='m3_project',
      version='1.0.0',
      url='https://github.com/valeriy-kirichenko/obt_test_task',
      license='BSD 3-Clause License',
      author='Valeriy Kirichenko',
      author_email='vmkirichenko1991@yandex.ru',
      description='test task',
      packages=find_packages(),
      long_description=open('../README.md').read(),
      zip_safe=False
)

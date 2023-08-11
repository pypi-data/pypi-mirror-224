from setuptools import setup, find_packages


setup(
    name='nixvenv',
    version='0.0.3',
    license='CC BY-NC-SA 4.0',
    author="TheCookingSenpai",
    author_email='administration@blockdrops.org',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/thecookingsenpai/nixvenv',
    keywords='unix linux macos mac venv environment virtual',
    install_requires=[],

)
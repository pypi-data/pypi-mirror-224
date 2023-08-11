from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = f.read()


setup(
    name='threed_optix',
    version='1.0.9',
    license='MIT',
    author="Elika Ron",
    author_email='alikaron@3doptix.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://3doptix.com',
    keywords='',
    install_requires=[
        'requests',
        'pandas',
        'matplotlib'
    ]
)

from setuptools import find_packages, setup

setup(
    name='testgear-adapter-robotframework',
    version='2.1.0',
    description='Robot Framework adapter for Test Gear',
    long_description=open('README.md', "r").read(),
    long_description_content_type="text/markdown",
    url='https://github.com/testgear-tms/adapters-python/',
    author='Integration team',
    author_email='integrations@test-gear.io',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    py_modules=['testgear_adapter_robotframework'],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=['attrs', 'robotframework', 'testgear-python-commons==2.1.0']
)

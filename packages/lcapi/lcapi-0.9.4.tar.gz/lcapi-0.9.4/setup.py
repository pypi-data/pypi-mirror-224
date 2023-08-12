from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='lcapi',
    version='0.9.4',
    description=(
        'A CLI client for the lc API.'
    ),
    url='https://github.com/unix-ninja/lcapi',
    author='unix-ninja',
    author_email='chris@unix-ninja.com',
    license='BSD',
    python_requires='>=3.9.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
             "lcapi=lcapi:main"
        ]
    },
    install_requires=[
        'requests'
        ]
    )

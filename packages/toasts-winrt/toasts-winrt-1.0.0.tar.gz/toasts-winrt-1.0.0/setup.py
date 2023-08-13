from setuptools import find_namespace_packages

from skbuild import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="toasts-winrt",
    version="1.0.0",
    description="Python WinRT bindings for Windows-Toasts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author='DatGuy',
    url="https://github.com/DatGuy1/toasts-winrt",
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Win32 (MS Windows)',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: System :: Operating System',
        ],
    python_requires=">=3.8",
    packages=find_namespace_packages(where="pywinrt"),
    package_dir={"": "pywinrt"},
    cmake_args=['-DCMAKE_BUILD_TYPE=Release', '-DCMAKE_C_COMPILER=cl', '-DCMAKE_CXX_COMPILER=cl'],
    # recursive glob (**) doesn't seem to work here
    package_data={"toasts_winrt": ["py.typed", "*.pyi", "*/*.pyi", "*/*/*.pyi", "*/*/*/*.pyi", "*/*/*/*/*.pyi"]},
)

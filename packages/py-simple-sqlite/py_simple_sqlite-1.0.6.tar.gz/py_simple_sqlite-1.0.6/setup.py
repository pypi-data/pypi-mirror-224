from setuptools import setup, find_packages

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(
    name='py_simple_sqlite',
    version='1.0.6',
    author='giperborei',
    description='Библиотека для упрощенной работы с sqlite',
    url='https://github.com/GiperBoreipy/ez_sqlite',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='python sqlite sql',
    python_requires='>=3.10'
)
from setuptools import setup, find_packages

setup(
    name='finanalyze',
    version='0.4.0',
    packages=find_packages(),
    install_requires=[
        'finnhub-python',
        'pandas',
        'numpy',
        'matplotlib'
    ],
    author='Manoj Kumar',
    author_email='manojkotary@gmail.com',
    description='A package for analyzing Financial Instruments like stocks.',
    long_description='A package for analyzing Financial Instruments like stocks.',
    url='https://github.com/MANOJ21K/FinOps/blob/main/custom_package',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

from setuptools import setup, find_packages

setup(
    name='stochasticparrot',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        'openai',
        'termcolor',
    ],
    author='Wes Ladd',
    author_email='wesladd@traingrc.com',
    description='A package for handling errors with custom logging that lets OpenAI API make suggestions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/custom_error_handler',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

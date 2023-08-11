from setuptools import setup, find_packages

setup(
    name='novellamemory',               # Replace 'my_package' with the actual package name
    version='1.0.2',
    description='A customize python package',
    author='Tuyen Tran',
    author_email='tuyentran0500@gmail.com',
    url='https://github.com/tuyentran0500/novella',  # Replace with your GitHub repository URL

    packages=find_packages(),       # Automatically find all packages in the project directory
    install_requires=[              # List the package dependencies here
        'langchain',
        'requests',
        'pydantic',
        'typing',
        'pymongo',
        'openai'
    ],

    # Add any other relevant metadata or configurations
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
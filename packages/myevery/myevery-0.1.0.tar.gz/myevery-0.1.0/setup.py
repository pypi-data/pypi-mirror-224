from setuptools import setup, find_packages

setup(
    name='myevery',
    version='0.1.0',
    description='A package to easily create and expose FastAPI services.',
    author='B. Truong',
    author_email='myevery@mail.com',
    url='https://github.com/myevery-ai/myevery',
    packages=find_packages(),
    install_requires=[
        'bs4',
        'loguru',
        'uvicorn[standard]',
        'fastapi',
        'fire'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

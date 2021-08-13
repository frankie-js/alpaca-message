from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='alpaca-message',
    version='1.0.0',
    author="Frankie J S",
    author_email="frankies.develop@gmail.com",
    description="A package that prints messages with alpacas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frankie-js/alpaca-message",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=['alpaca'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'alpaca-message = alpaca:main',
        ],
    },
    python_requires=">=3.9",
)

from setuptools import setup, find_packages

setup(
    name="password-manager",
    version="1.0.0",
    author="heheboi",
    author_email="heheboi@mail.com",
    description="A simple password manager",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BU77ERFLY-3FF3C7/password-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pyperclip",
        "tk",
    ],
    entry_points={
        "console_scripts": [
            "password-manager=password_manager.main:main",
        ],
    },
)


from setuptools import setup, find_packages

setup(
    name="myactuator_lib",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        'python-can','numpy'
    ],
    author="Nathan Adkins",
    author_email="npa00003@mix.wvu.edu",
    description="Defines classes for controlling myactuator motors.",
    license="MIT",
    keywords="actuator myactuator robotics",
    url="https://github.com/wvu-urc/myactuator_lib",   # project homepage
)
from setuptools import setup, find_packages

setup(
    name='django-ipchecker',
    version='0.1',
    description='A Django package to check IP addresses.',
    author='Your Name',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
)

from setuptools import setup

setup(
    name='twitterAPI-sentiment',
    version='0.1.0',
    description='Analyzes the sentiment of tweets about any topic',
    author='Aleksandr',
    author_email='novacyan545@gmail.com',
    packages=['src', 'my_package'],
    install_requires=[
        'tweepy',
        'textblob',
    ],
)

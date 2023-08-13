import setuptools


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setuptools.setup(
    name='text_randomizer',
    version='0.0.1',
    author='Timur Zolotov TZbooo netbiom',
    author_email='helloworldbooo@gmail.com',
    long_description=readme(),
    long_description_content_type='text/markdown',
    description='Implementation of templating random values inside text',
    packages=['text_randomizer'],
    maintainer='https://github.com/TZbooo',
    maintainer_email='helloworldbooo@gmail.com'
)

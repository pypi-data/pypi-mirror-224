from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='lealtictactoe',
    version='0.0.1',
    license='MIT License',
    author='José Rodolfo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='silvaleal.ctt@gmail.com',
    keywords='lealtictactoe',
    description=u'Uma IA para nunca perder no jogo da velha',
    packages=['lealtictactoe'],
    install_requires=[])
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ai_music_composer",
    version="0.1.0",
    author="Sushant",
    description="An AI Music Composer application",
    packages=find_packages(),
    install_requires=requirements
)
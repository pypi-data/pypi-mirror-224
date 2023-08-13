from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pyppeteer==1.0.2", "pyppeteer_stealth==2.7.4"]

keywords = [
    "python",
    "python3",
    "api",
    "characterai",
    "character.ai",
    "beta.character.ai",
]

setup(
    name="KirbacterAI",
    version="1.0.0",
    author="KirbyRedius",
    author_email="",
    description="API Library for beta.character.ai",
    long_description=readme,
    url="https://github.com/KirbyRedius/CharacterAI/",
    packages=find_packages(),
    install_requires=requirements,
    keywords=keywords
)
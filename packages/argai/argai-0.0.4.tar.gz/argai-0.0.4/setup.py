from setuptools import find_packages, setup
from argai import __version__

core_reqs = [
    "openai",
    "requests",
    "pydantic"
]

setup(
    name="argai",
    description="Make any of your functions queryable with natural language.",
    version=__version__,
    url="https://arg.ai/",
    author="Jacky Koh",
    author_email="jacky@arg.ai",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    setup_requires=["wheel"],
    install_requires=core_reqs,
    package_data={"": ["*.ini"]},
    extras_require=dict(),
)

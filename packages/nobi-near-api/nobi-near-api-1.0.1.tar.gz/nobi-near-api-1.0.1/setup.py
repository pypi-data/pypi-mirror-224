from setuptools import setup, find_packages

META_DATA = dict(
    name="nobi-near-api",
    version="1.0.1", #  forked from 0.1.0 near-api
    license="MIT",

    author="NEAR Inc",

    url="https://github.com/nobbennob/nobi-near-api",

    packages=find_packages(),

    install_requires=["requests", "base58", "ed25519"]
)

if __name__ == "__main__":
    setup(**META_DATA)

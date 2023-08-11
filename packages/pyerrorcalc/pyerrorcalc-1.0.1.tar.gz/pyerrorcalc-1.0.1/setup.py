from setuptools import setup,find_packages

setup(
    name = "pyerrorcalc",
    version = "1.0.1",
    author = "Philip",
    author_email="<digests-earnest.0r@icloud.com>",
    description="Error calculation",
    long_description="Compute errors with gaussian or minmax method",
    packages=find_packages(),
    install_requires=["sympy"]
)



import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="platon",
    version="1.1.beta",
    author="Michael Zhang, Yayaati Chachan, Eliza Kempton",
    author_email="zmzhang@caltech.edu",
    description="A package to compute transmission spectra and retrieve atmospheric parameters from transmission spectra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ideasrule/platon",
    download_url="https://github.com/ideasrule/platon/archive/beta.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    include_package_data = True,
    zip_safe = False
)

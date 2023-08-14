from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.9'
DESCRIPTION = 'Python functions to download favicons using internal google api'
LONG_DESCRIPTION = """
# grab_favicon

Python functions to download favicons using internal google api

## Installation

Install function by running the following command.

```bash
  pip install grab_favicon
```

## Usage/Examples

```python
from grab_favicon import download_favicon, download_favicons

# Single download
download_favicon("google.com", size=128)

# Multiple downloads
websites = ["google.com", "stackoverflow.com", "github.com"]
download_favicons(websites, path="my/path/favicons")
```

NOTE: The file is saved to a directory under the name *website.com*.png

## Acknowledgements
- [aanupam23](https://github.com/aanupam23/FaviconGrabber/tree/main)"""

# Setting up
setup(
    name="grab_favicon",
    version=VERSION,
    author="Emilio Mendoza",
    author_email="emen3998@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'favicon', 'downloader', 'grabber'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

# dep2req

## Overview

With `dep2req` you can extract dependencies from `pyproject.toml` files to `requirements.txt` in seconds. No more waiting for `pip-compile` to finish. 

## Installation

```
pip install dep2req
```

## Usage

Simply run in any directory containing a `pyproject.toml` file: 

```
dep2req
```` 

and a `requirements.txt` will be created in the current working directory.

```
usage: dep2req [-h] [-f FILENAME] [-a] [-s OPTIONAL_SECTIONS]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Path to the input pyproject.toml file
  -a, --add-optional    Whether to include "optional-dependencies" [defaults
                        to including all sections]
  -s OPTIONAL_SECTIONS, --optional-sections OPTIONAL_SECTIONS
                        Name(s) of "optional-dependencies" section(s) to
                        include, comma-delimited
```


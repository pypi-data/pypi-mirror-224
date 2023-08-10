
# Install the library

Clone the repository

```shell
git clone https://github.com/GIALaboratory/cloud-platform-engineering.git
```

Move into the `library` directory

```shell
cd cloud-platform-engineering/githubauthlib
```

Install the library

```shell
pip install .
```

This is the expected output:

```shell
Processing /Users/gconklin/github.com/GIALaboratory/cloud-platform-engineering/githubauthlib
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: githubauthlib
  Building wheel for githubauthlib (setup.py) ... done
  Created wheel for githubauthlib: filename=githubauthlib-0.1-py3-none-any.whl size=966 sha256=61c794e5afbc49de35d0c98020921c4bed29f463c70e2db3071cafcd1fa09e42
  Stored in directory: /private/var/folders/m6/tqrb8gq551q5y32zqmkj1vbw0000gr/T/pip-ephem-wheel-cache-2fcchk2x/wheels/00/32/55/351188001c24d6b3d4dbc24e22cdf1119f26fda745d7dc777b
Successfully built githubauthlib
Installing collected packages: githubauthlib
Successfully installed githubauthlib-0.1
```

Take a look at what is there now

```shell
$ pip list |grep githubauthlib
githubauthlib         0.1

$ pip show githubauthlib
Name: githubauthlib
Version: 0.1
Summary: 
Home-page: 
Author: 
Author-email: 
License: 
Location: /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages
Requires: 
Required-by:
```

Add the path to the `githubauthlib` directory to your `$PYTHONPATH` environment variable

```shell
# PATH additions
export PYTHONPATH="${PYTHONPATH}:/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/githubauthlib-0.1.dist-info:~/github.com/GIALaboratory/cloud-platform-engineering/githubauthlib"
```

See also [AUXILIARY.md](AUXILIARY.md)

What the directory looks like

```shell
githubauthlib/
.
├── AUXILIARY.md
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-311.pyc
│   └── github_auth.cpython-311.pyc
├── build
│   └── bdist.macosx-10.9-universal2
├── github_auth.py
├── githubauthlib.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
└── setup.py

5 directories, 11 files
```

Now, in any Python script on your system, you can use the library :)

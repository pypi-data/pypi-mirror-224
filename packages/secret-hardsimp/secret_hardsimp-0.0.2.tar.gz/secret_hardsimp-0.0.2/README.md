---
title: Secrit
---

Introduction
============

Secrit is a simple Python library designed to interact with the \'pass\'
password store generated keys.

Installation
============

First, ensure that you have the \`\~/.password-store/\` directory
available as the library uses it as the default storage path.

To install the Secrit library, you can simply use pip:

``` {.bash}
pip install secrit
```

Usage
=====

Retrieve a Password
-------------------

To retrieve a decrypted content of a password store entry, use the
\`get\` function:

``` {.python}
import secrit

# You will be prompted for your master password
api_key = secrit.get("github.com/api_key")
```

Requirements
============

-   Python 3
-   python-gnupg

Development
===========

To contribute or report issues, please visit the [GitHub
repository](https://github.com/hard-simp/secrit.py).

License
=======

MIT

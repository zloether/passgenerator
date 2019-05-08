# PassGenerator
[![Python](https://img.shields.io/pypi/pyversions/passgenerator.svg)](https://www.python.org/)
[![Build Status](https://travis-ci.org/zloether/PassGenerator.svg?branch=master)](https://travis-ci.org/zloether/PassGenerator)
[![Issues](https://img.shields.io/github/issues/zloether/passgenerator.svg)](https://github.com/zloether/passgenerator/issues)
[![License](https://img.shields.io/github/license/zloether/passgenerator.svg)](https://opensource.org/licenses/MIT)

`PassGenerator` is a secure password generator with a CLI utility.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
    - [Command Line Utility](#command-line-utility)
- [License](#license)

## Prerequisites
You'll need to have Python installed in order to run `PassGenerator`. Start by downloading and installing [Python](https://www.python.org/downloads/).
> *Note: Python 3 is recommended, however `PassGenerator` has been successfully tested with Python 2.6+*


## Installation
```
pip install passgenerator
```

## Usage
`PassGenerator` provides the following methods:
```
passgenerator.generate(length=32, upper=True, lower=True, numbers=True, special=True)
passgenerator.phoenetic(number_words=4, word_list='path/to/list')
```

Sample code:
```
>>> import passgenerator
>>> passgenerator.generate()
'qq*6opDb45;o~;6jWy4U-A5V.*cbHp1Z'
>>> passgenerator.generate(14, numbers=False)
"N'VJXGQ'Sj)Cj-"
>>> passgenerator.phoenetic()
('calliper delaying shrunken crednerite', 'calliperdelayingshrunkencrednerite')
>>> passgenerator.phoenetic(6)
('airproofs octohedral cryptopyic parabled supervigorous laparomyomotomy', 'airproofsoctohedralcryptopyicparabledsupervigorouslaparomyomotomy')
```


### Command Line Utility
`PassGenerator` includes a command line utility for generating passwords.
```
passgenerator --help
usage: passgenerator.py [-h] [-l] [-L] [-n] [-N] [-p] [-s] [-S] [-u] [-U]
                        [-w <word list>]
                        [length]

Generates secure random passwords

positional arguments:
  length                length of password (default is 32 characters for
                        gibberish and 4 words for phoenetic)

optional arguments:
  -h, --help            show this help message and exit
  -l, --lower-enable    use lower case characters
  -L, --lower-disable   don't use lower case characters
  -n, --number-enable   use number characters
  -N, --number-disable  don't use number characters
  -p, --phoenetic       create phoenetic password using English words
  -s, --special-enable  use special characters
  -S, --special-disable
                        don't use special characters
  -u, --upper-enable    use upper case characters
  -U, --upper-disable   don't use upper case characters
  -w <word list>, --word-list <word list>
                        use provided word list (plaintext format, return
                        seperated

optional argument '-w/--word-list' assumes '-p/--phoenetic'
```

Generating a default password:
```
passgenerator
zT0Q9tyfcAx.S2d8*pXGxen86ipSL_;E
```

Generating a 14 character password with no special characters:
```
passgenerator -S 14
pocUvtR0RyZ9jd
```



## License

This project is licensed under the MIT License

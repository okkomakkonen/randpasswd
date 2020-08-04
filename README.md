# Random passphrase generator

This program can generate a random passpharse using a wordlist from [Diceware](http://world.std.com/~reinhold/diceware.wordlist.asc). Use this program by running the following command.
```bash
$ randpasswd
$ randpasswd --length 7 --sep _
```

### Usage

You can use the following options.
```bash
usage: randpasswd [-h] [-l LENGTH] [-s SEP] [--bits-of-security]

optional arguments:
  -h, --help            show this help message and exit
  -l LENGTH, --length LENGTH
                        number of words to use in passphrase (default 6)
  -s SEP, --sep SEP     separator character to use (default " ")
  --bits-of-security    show the security of a password
```
See this help page with
```bash
$ randpasswd --help
```

## Installation

Clone this git repository and run
```bash
$ pip install .
```

Install directly from git with
```bash
$ pip install git+https://github.com/okkomakkonen/randpasswd.git
```

#### Bits of security

The dictionary used has 7776 words or special characters. The bits of security in the passphrase is then `length * log2(7776)`. For a 6 word passphrase that is 77 bits of security. The following command will show how many bits other passwords have
```bash
$ randpasswd --length 7 --bits-of-security
```

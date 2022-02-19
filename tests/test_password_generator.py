"""
Tests password generator
"""
from randpasswd import generate_random_password, wordlist
from string import digits


def test_in_wordlist():

    length, sep = 7, " "

    for _ in range(1000):

        password = generate_random_password(length, sep)

        assert all(word in wordlist for word in password.split(sep))


def test_different():

    length, sep = 7, "+"

    assert len(set(generate_random_password(length, sep) for _ in range(1000))) == 1000


def test_num():

    length, sep = 7, " "

    passwords = generate_random_password(length, sep, ensure_num=True)

    assert all(any(d in password for d in digits) for password in passwords)

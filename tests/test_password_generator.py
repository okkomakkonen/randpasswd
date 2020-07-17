"""
Tests password generator
"""
from randpasswd import generate_random_password, wordlist


def test_in_wordlist():

    length, sep = 7, " "

    for _ in range(1000):

        password = generate_random_password(length, sep)

        assert all(word in wordlist for word in password.split(sep))


def test_different():

    length, sep = 7, "+"

    assert len(set(generate_random_password(length, sep) for _ in range(1000))) == 1000

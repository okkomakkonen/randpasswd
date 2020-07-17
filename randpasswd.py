"""
Generate a random passphrase using diceware wordlist
"""
import secrets
from typing import List
import argparse
from math import log2

WORDLIST_FILENAME = "wordlist.txt"

wordlist: List[str] = []
with open(WORDLIST_FILENAME, "r") as f:
    for line in f:
        wordlist.append(line.strip().split()[1])


def generate_random_password(length: int, sep: str = " ") -> str:
    """ Generates a random password using length words from the wordlist separated by sep """

    return sep.join(secrets.choice(wordlist) for _ in range(length))


def bits_of_security(length: int) -> float:
    """ Return the bits of security a password of length has """
    return length * log2(len(wordlist))


def main():
    """ Parses CLI arguments and prints out generated password """

    parser = argparse.ArgumentParser(prog="randpasswd")
    parser.add_argument("-l", "--length", type=int, default=6)
    parser.add_argument("-s", "--sep", type=str, default=" ")
    parser.add_argument("--bits-of-security", action="store_true")

    args = parser.parse_args()

    if args.bits_of_security:
        print(
            f"Using a password of length {args.length} has a security of {bits_of_security(args.length)} bits."
        )
    else:
        print(generate_random_password(args.length, args.sep))


if __name__ == "__main__":
    main()

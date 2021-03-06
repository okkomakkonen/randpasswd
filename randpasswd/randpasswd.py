"""
Generate a random passphrase using diceware wordlist
"""
import sys
import secrets
from typing import List
import argparse
from math import log2
import pathlib

WORDLIST_FILENAME = pathlib.Path(__file__).parent.absolute() / "wordlist.txt"

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
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=6,
        help="number of words to use in passphrase (default 6)",
    )
    parser.add_argument(
        "-s",
        "--sep",
        type=str,
        default=" ",
        help='separator character to use (default " ")',
    )
    parser.add_argument(
        "--bits-of-security",
        action="store_true",
        help="show the security of a password",
    )

    args = parser.parse_args()

    if args.bits_of_security:
        print(
            f"Using a password of length {args.length} has a security of {bits_of_security(args.length)} bits."
        )
    else:
        print(generate_random_password(args.length, args.sep))

    sys.exit(0)


if __name__ == "__main__":
    main()

"""
Generate a random passphrase using diceware wordlist
"""
import sys
import secrets
from typing import List
import argparse
from math import log2
import pathlib
from enum import Enum
from string import digits


class Case(Enum):
    LOWER, UPPER, TITLE = range(3)


WORDLIST_FILENAME = pathlib.Path(__file__).parent.absolute() / "wordlist.txt"

wordlist: List[str] = []
with open(WORDLIST_FILENAME, "r") as f:
    for line in f:
        wordlist.append(line.strip().split()[1])

num_words = len(wordlist)
num_words_with_nums = len([w for w in wordlist if any(d in w for d in digits)])


def generate_random_password(
    length: int, sep: str = " ", case: Case = Case.LOWER, ensure_num: bool = False
) -> str:
    """ Generates a random password using length words from the wordlist separated by sep """
    password = ""
    while (not password and not ensure_num) or not any(d in password for d in digits):
        if case == Case.LOWER:
            password = sep.join(secrets.choice(wordlist) for _ in range(length))
        elif case == Case.UPPER:
            password = sep.join(secrets.choice(wordlist).upper() for _ in range(length))
        elif case == Case.TITLE:
            password = sep.join(secrets.choice(wordlist).title() for _ in range(length))
        else:
            raise ValueError("not a valid case")
    return password


def bits_of_security(length: int, ensure_num: bool = False) -> float:
    """ Return the bits of security a password of length has """
    if not ensure_num:
        return length * log2(num_words)
    else:
        return log2(num_words ** length - (num_words - num_words_with_nums) ** length)


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
    parser.add_argument(
        "--ensure-num", action="store_true", help="ensure that password has a number"
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--lower", action="store_true", help="lowercase")
    group.add_argument("--upper", action="store_true", help="uppercase")
    group.add_argument("--title", action="store_true", help="titlecase")

    args = parser.parse_args()

    if args.lower:
        case = Case.LOWER
    elif args.upper:
        case = Case.UPPER
    elif args.title:
        case = Case.TITLE
    else:
        case = Case.LOWER

    if args.bits_of_security:
        if not args.ensure_num:
            print(
                f"Using a password of length {args.length} has a security of {bits_of_security(args.length):.1f} bits."
            )
        else:
            print(
                f"Using a password of length {args.length} with a number has a security of {bits_of_security(args.length, ensure_num=True):.1f} bits."
            )
    else:
        print(
            generate_random_password(
                args.length, args.sep, case=case, ensure_num=args.ensure_num
            )
        )

    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
Project for UFCD 9190: Introduction to Programming Applied to Cybersecurity

(c) João Cidade Silva, 2024 | November 30 .v1

PyCracker attempts to "crack" a password file with a structure similar to `/etc/shadow`.
It provides two ways to handle command-line arguments:
    1. Using the `argparse` module from the standard library.
    2. Using the `docopt` module (available on PyPI).
"""

import random
import string
import sys
from enum import Enum
from typing import TextIO
from docopt import docopt
from textwrap import dedent
import passlib.exc
from passlib.hash import sha512_crypt
from passlib.context import CryptContext

# Default shadow-like file
DEFAULT_PWD_FILE = "/etc/shadow"

# Passlib CryptContext configuration
PYCRACKER_CTX = CryptContext(
    schemes=["sha512_crypt", "sha256_crypt", "md5_crypt", "sha1_crypt", "bcrypt"]
)

# Mapping of hash IDs to names
HASH_ID_NAMES = {
    "1": "MD5",
    "2": "Blowfish",
    "2a": "Blowfish (2a)",
    "2b": "Blowfish (2b)",
    "5": "SHA-256",
    "6": "SHA-512",
}

# Account statuses
AccountStatus = Enum("AccountStatus", "VALID BLOCKED LOCKED INVALID")


def show_matches(
    pwd_filename: str, dict_filename: str, user: str | None = None, verbose=False
):
    """
    Display all decrypted passwords and users.
    """
    matches = find_matches(pwd_filename, dict_filename, user, verbose)
    if len(matches) == 0:
        print("No passwords were found.")
    else:
        print("The following passwords were found for users:")
        for user, (clear_text_pwd, method_name) in matches.items():
            print(f"[+] {user:10}: {repr(clear_text_pwd):<20} ({method_name})")


def find_matches(
    pwd_filename: str, dict_filename: str, user: str | None = None, verbose=False
) -> dict[str, tuple[str, str]]:
    """
    Returns a dictionary mapping each username to their decrypted password and the hashing method.
    """
    matches = {}
    with open(pwd_filename, "rt") as pwd_file:
        with open(dict_filename, "rt") as dict_file:
            for line in pwd_file:
                curr_user, pwd_field = line.split(":")[:2]

                # Skip accounts with invalid statuses
                account_status = get_account_status(pwd_field)
                if account_status is not AccountStatus.VALID:
                    if verbose:
                        print(
                            f"[!] Skipping user {curr_user}: Account status is {account_status.name}"
                        )
                    continue

                # Check if the hash method is known
                if method_name(pwd_field) == "Unknown":
                    if verbose:
                        print(
                            f"[!] Skipping user {curr_user}: Unknown hash format {pwd_field}"
                        )
                    continue

                # Attempt to find the password
                clear_text_pwd = find_pwd(pwd_field, dict_file)
                if clear_text_pwd:
                    matches[curr_user] = (clear_text_pwd, method_name(pwd_field))
                    if verbose:
                        print(f"[+] Match found for user {curr_user}: {clear_text_pwd}")

                # Reset dictionary file pointer for next user
                dict_file.seek(0)

    return matches


def get_account_status(pwd_field: str) -> AccountStatus:
    """
    Determine the account status based on the password field.
    """
    return (
        AccountStatus.BLOCKED
        if pwd_field in ("*", "!")
        else (
            AccountStatus.LOCKED
            if len(pwd_field) > 0 and pwd_field[0] == "!"
            else AccountStatus.INVALID if len(pwd_field) == 0 else AccountStatus.VALID
        )
    )


def find_pwd(pwd_field: str, dict_file: TextIO) -> str | None:
    """
    Search for a clear-text password in `dict_file` that hashes to the same value as `pwd_field`.
    Returns the clear-text password if found, otherwise `None`.
    """
    for clear_text_pwd in dict_file:
        clear_text_pwd = clear_text_pwd.strip()
        try:
            if verify_password(clear_text_pwd, pwd_field):
                return clear_text_pwd
        except passlib.exc.UnknownHashError:
            # Ignore unknown hash errors
            continue
    return None


def verify_password(clear_text_pwd: str, pwd_field: str) -> bool:
    """
    Verify if the clear-text password matches the hash.
    """
    try:
        return PYCRACKER_CTX.verify(clear_text_pwd, pwd_field)
    except passlib.exc.UnknownHashError:
        print(f"Unknown hash: {pwd_field}")
        return False


def method_name(pwd_field: str) -> str:
    """
    Extract the hashing method name from the password field.
    """
    parsed = parse_pwd_field(pwd_field)
    if not parsed:
        return "Unknown"
    method_id = parsed[0]
    return HASH_ID_NAMES.get(method_id, "Unknown")


def parse_pwd_field(pwd_field: str) -> tuple | None:
    """
    Parse the password field into method, salt, and hash components.
    """
    if not pwd_field.startswith("$"):
        return None  # Invalid format
    try:
        parts = pwd_field.strip("$").split("$", 2)
        if len(parts) != 3:
            return None  # Invalid format
        return tuple(parts)
    except ValueError:
        return None


def encrypt_pwd_for_shadow(clear_text_pwd: str, salt_size=8) -> str:
    """
    Generate a shadow-compatible password field using SHA-512.
    """
    SHA512_ROUNDS = 5000
    salt_chars = string.ascii_letters + string.digits
    salt = "".join(random.choice(salt_chars) for _ in range(salt_size))
    return sha512_crypt.using(salt=salt, rounds=SHA512_ROUNDS).hash(clear_text_pwd)


def main1():
    """
    Entry point using the docopt library.
    """
    doc = dedent(
        f"""
    PyCracker is a password cracker written in Python3. Using a password dictionary, it searches for user with passwords in that dictionary.

    Usage:
        {sys.argv[0]} <dictionary> [<passwords>] [-u USER] [-v]

    Options:
        -h, --help              Show this help message.
        <passwords>             /etc/shadow-like file [default: {DEFAULT_PWD_FILE}]
        <dictionary>            Password dictionary.
        -u USER, --user=USER    Search passwords for this USER only.
        -v, --verbose           Increase verbosity level.
    """
    )

    args = docopt(doc)
    pwd_file = args["<passwords>"] or DEFAULT_PWD_FILE
    show_matches(pwd_file, args["<dictionary>"], args["--user"], args["--verbose"])


def main2():
    """
    Entry point using the argparse library.
    """
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Password Cracker")
    parser.add_argument(
        "dictionary",
        help="File containing a password dictionary.",
        metavar="<dictionary>",
    )
    parser.add_argument(
        "passwords",
        help="File similar to /etc/shadow.",
        metavar="<passwords>",
        nargs="?",
        default=DEFAULT_PWD_FILE,
    )
    parser.add_argument(
        "-u",
        "--user",
        help="Target specific user. If none is provided, try all.",
        required=False,
    )
    parser.add_argument(
        "-v", "--verbose", help="Increase verbosity level.", action="store_true"
    )
    args = parser.parse_args()

    show_matches(args.passwords, args.dictionary, args.user, args.verbose)


if __name__ == "__main__":
    main2()

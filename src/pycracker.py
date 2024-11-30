#!/usr/bin/env python3

"""
Project for UFCD 9190: Introduction to Programming Applied to Cybersecurity

(c) João Cidade Silva, 2024

Tenta 'crackar' um ficheiro de palavras-passe com estrutura idêntica ao '/etc/shadow'. Apresentam-se aqui as duas formas de ler parâmetros da linha de comandos:
    1. Utilizando o módulo argparse (presente na biblioteca padrão)
    2. Utilizando o módulo docopt (disponível no PyPI)
"""

import sys
from pprint import pprint
from typing import TextIO
from docopt import docopt
from textwrap import dedent

from passlib.hash import (
    sha512_crypt,
    #sha256_crypt,
    #md5_crypt,
    #sha1_crypt,
    #bcrypt,
)
from passlib.context import CryptContext

DEFAULT_PWD_FILE = "/etc/shadow"

PYCRACKER_CTX = CryptContext(schemes = [
    'sha512_crypt',
    'sha256_crypt',
    'md5_crypt',
    'sha1_crypt',
    'bcrypt',
])

def show_matches(
        pwd_filename: str,
        dict_filename: str,
        user: str | None = None,
        verbose = False,
):
    """
    Shows all decrypted passwords and users.
    """
    matches = find_matches (pwd_filename, dict_filename, user, verbose)
    if len(matches) == 0:
        print("Não foram encontradas quaisquer palavras-passe")
    else:
        print(f"Foram encontradas as seguintes palavras-passe: {matches}")
#:

def find_matches(
        pwd_filename: str,
        dict_filename: str,
        user: str | None = None,
        verbose = False,        
) -> dict[str, tuple[str, str]]:
    """
    Returns a dictionary where each entry maps a username to a decrypted password and the hashing algorithm that was used to encrypt the password.
    """
    matches = {}
    with open (pwd_filename, 'rt') as pwd_file:
        with open(dict_filename, 'rt') as dict_file:
            for line in pwd_file:
                curr_user, pwd_field =  line.split(':')[:2]
                if clear_text_pwd := find_pwd(pwd_field, dict_file):
                    matches[curr_user] = clear_text_pwd
    return matches
#:

def find_pwd(pwd_field: str, dict_file: TextIO) -> str | None: 
    """
    This function searches for a clear-text password in `dict_file` that hashesnto the same value as the hash in `pwd_field`.
    Returns the clear-text password, if one is found, otherwise returns `None`.

    `pwd_field` is the password fiels for a given user in a /etc/shadow-like file. Example:
    $6$m7.33qCr$joi9qE/ZY...etc...7NqU4/LWYUiP9kxZIoJ90KJRm.
    """
    for clear_text_pwd in dict_file:
        clear_text_pwd = clear_text_pwd.strip()
        if verify_password(clear_text_pwd, pwd_field):
            return clear_text_pwd
    return None
#:

def verify_password(clear_text_pwd: str, pwd_field: str) -> bool:
    return PYCRACKER_CTX.verify(clear_text_pwd, pwd_field)
#:

def main1():
    """
    PyCracker entry point. Reads comand line arguments and using the docopt library and calls the appropriate functions.
    """

    doc = dedent(f"""
    PyCracker is a password cracker written in Python3. Using a password dictionary, it searches for user with passwords in that dictionary.

    Usage:
        {sys.argv[0]} <dictionary> [<] [<passwords>] [-u User] [-v]

    Options:
        -h, --help              Show help
        <passwords>             /etc/shadow-like file [default: default: '{DEFAULT_PWD_FILE}']
        <dictionary>            Password dictionary
        -u USER, --user=USER    Search password for this USER only
        -v, --verbose           Increase verbosity level
    """)

    args = docopt(doc)
    pwd_file = args['<passwords>'] or DEFAULT_PWD_FILE
    show_matches(pwd_file, args['<dictionary>'], args['--user'], args['--verbose'])
#:

def main2():
    """
    PyCracker entry point. Reads comand line arguments and using the argparse library and calls the appropriate functions.
    Basiamente é isto mas em inglês, deve-se alterar, integrar na linha de cima: Lê e interpreta argumentos de entrada com ARGPARSE e inicia a descodificação
    """
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Password Cracker")
    parser.add_argument(
        'dictionary',
        help="Ficheiro com dicionário de palavras-passes.",
        metavar='<dictionary>'
    )
    parser.add_argument(
        'passwords',
        help="A file similar to /etc/shadow.",
        metavar='<passwords>',
        nargs='?',
        default=DEFAULT_PWD_FILE,
    )
    parser.add_argument(
        '-u', '--user',
        help="User. If none is passed, try all.",
        required=False,
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Increase verbosity level.",
        action ='store_true',
    )
    args = parser.parse_args()
    #print(args.passwords, args.dictionary, args.user, args.verbose)
    # TODO: falta chamar a função para exibir resultados
    show_matches(args.passwords, args.dictionary, args.user, args.verbose)
#:

if __name__ == "__main__":
    main2()

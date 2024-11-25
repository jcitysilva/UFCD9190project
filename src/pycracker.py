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
from docopt import docopt

DEFAULT_PWD_FILE = '/etc/shadow'

def main():
    """
    PyCracker entry point. Reads comand line arguments and using the docopt library calls the appropriate functions.
    """

    doc = f"""
    PyCracker is a password cracker written in Python3. Using a password dictionar, it searches for user with passwords in that dictionary.

    Usage:
        {sys.argv[0]} <dictionary> [<] [<passwords>] [-u User] [-v]

    Options:
        -h, --help              Show help
        <passwords>             /etc/shadow-like file [default: {DEFAULT_PWD_FILE}]
        <dictionary>            Password dictionary
        -u USER, --user=USER    Search password for this USER only
        -v, --verbose           Increase verbosity level
    """

    args = docopt(doc)
    print(args)
#:

if __name__ == '__main__':
    main()
#!/usr/bin/env python3

"""
Project for UFCD 9190: Introduction to Programming Applied to Cybersecurity

(c) João Cidade Silva, 2024

Tenta 'crackar' um ficheiro de palavras-passe com estrutura idêntica ao '/etc/shadow'. Apresentam-se aqui as duas formas de ler parâmetros da linha de comandos:
    1. Utilizando o módulo argparse (presente na biblioteca padrão)
    2. Utilizando o módulo docopt (disponível no PyPI)
"""

import os
import re
import hashlib
from pprint import pprint
from docopt import docopt

def main():
    """
    PyCracker entry point. Reads comand line arguments and using the docopt library calls the appropriate functions.
    """

    doc = """
    PyCracker is a password cracker written in Python3. Using a password dictionar, it searches for user with passwords in that dictionary.

    Usage:
    """

if __name__ == '__main__':
    main()
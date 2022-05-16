#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada  ex;

    export LANG=pt_BR

Execucao: 
    
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Victor"
__license__ = "Unlicense"


current_language = "it_IT"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Ola, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo"

print(msg)





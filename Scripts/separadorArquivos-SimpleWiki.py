#FEITO POR LEVI MATHEUS
#ESTE CODIGO ENTRA NA PASTA A PARTIR DO DIRETORIO ATUAL E
#PEGA TODOS OS ARQUIVOS DENTRO DELA E SEPARA OS ARTIGOS EM NOVOS ARQUIVOS DE TEXTO
#UTILIZADO PARA USAR EM ARQUIVOS DE SAIDA DO SCRIPT PREPROCESSADOR

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
        pprint("###### DIRETÓRIO ATUAL: " + os.getcwd() + " ######")
        ext = ".txt"
        pprint("###### INICIANDO A LEITURA DOS ARQUIVOS ######")
        arquivo = open(nomearq + ext, "r", encoding="utf8")
        linhas = arquivo.readlines()
        arquivo.close()
        pprint("###### FIM LEITURA DOS ARQUIVOS ######")
        ext = ".txt"
        pprint("###### CRIANDO DIRETORIO DE SAIDA ######")
        os.mkdir('./textos')
        os.chdir('./textos/')
        pprint("###### INICIANDO SEPARAÇÃO DOS ARQUIVOS ######")
        novalinha = True
        for key, linha in enumerate(linhas):
            #firstWord = linhas[:][0]
            #firstWord = firstWord.strip('\n')
            if linha.strip() == '':
                novalinha = True
            else:
                if(novalinha):
                    novalinha=False
                    firstWord = linha[:]
                    firstWord = firstWord.strip('\n')
                    firstWord = firstWord.replace("\\","")
                    firstWord = firstWord.replace("/", "")
                    firstWord = firstWord.replace(" ", "_")
                    firstWord = firstWord.replace("*", "_")
                    firstWord = firstWord.replace('"', "'")
                    firstWord = firstWord.replace('?','')
                    novo_arq = open(str(firstWord) + ext, "a", encoding="utf8")
                else:
                    #novo_arq = open(str(firstWord) + ext, "a", encoding="utf8")
                    novo_arq.write(linha)
        pprint("###### FIM PREPROCESSAMENTO ######")
        novo_arq.close()
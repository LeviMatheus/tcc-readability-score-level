#FEITO POR LEVI MATHEUS
#ESTE CODIGO ENTRA NA PASTA A PARTIR DO DIRETORIO ATUAL E
#PEGA TODOS OS ARQUIVOS DENTRO DELA E SEPARA OS ARTIGOS EM NOVOS ARQUIVOS DE TEXTO
#UTILIZADO PARA USAR EM ARQUIVOS DE SAIDA DO SCRIPT PREPROCESSADOR

import os
import sys
import fileinput
from pprint import pprint

ext_validas = [""]

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
        ext = ""
        pprint("###### INICIANDO A LEITURA DOS ARQUIVOS ######")
        pprint("nome: " + nomearq + ext)
        arquivo = open(os.getcwd() + "\\" + nomearq + ext, "r", encoding="utf8")
        linhas = arquivo.readlines()
        arquivo.close()
        pprint("###### FIM LEITURA DOS ARQUIVOS ######")
        ext = ".txt"
        if(not os.path.isdir(os.getcwd() + '//textos')):
            pprint("###### CRIANDO DIRETORIO DE SAIDA ######")
            os.mkdir('./textos')
        os.chdir('./textos/')
        pprint("###### INICIANDO SEPARAÇÃO DOS ARQUIVOS ######")
        novalinha = True
        for key, linha in enumerate(linhas):
            #firstWord = linhas[:][0]
            #firstWord = firstWord.strip('\n')
            if '<doc id=' in linha:
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
                    print("nome novo arquivo: " + str(firstWord) + ext)#para debugar
                    novo_arq = open(str(firstWord) + "_" + ext, "a+", encoding="utf8")
                else:
                    #novo_arq = open(str(firstWord) + ext, "a", encoding="utf8")
                    if '</doc>' in linha:
                        novo_arq.write('')
                    else:
                        novo_arq.write(linha)
        pprint("###### FIM PREPROCESSAMENTO ######")
        novo_arq.close()
        os.chdir('../')
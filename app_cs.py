#-*- coding: utf-8 -*-
import tadchoiceset

'''
  Aplicação para testar o tad choiceset e investigar o conceito de choiceset e objetos de fluxo (ofs).
  28/11/2017
  v1.0
  Ernani & Mateus
'''
def main():
    dados_cs = ["A", "B", "C"]

    var_cs = tadchoiceset.create_cs(dados_cs)

    print(tadchoiceset.to_string(var_cs))

    return 0
# fim main

main()


#-*- coding: utf-8 -*-
import tadchoiceset

'''
  Aplicação que testa o tad choiceset e explora os conceitos de choiceset e objetos de fluxo (ofs).
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


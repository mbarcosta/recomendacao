#-*- coding: utf-8 -*-
import tadchoiceset as cs

'''
  Aplicação que testa o tad choiceset e explora os conceitos de choiceset e objetos de fluxo (ofs).
  28/11/2017
  v1.0
  Ernani & Mateus
'''
def main():
    str_val_cs = "A, B, C, D"

    var_cs_A = cs.create_str(str_val_cs)
    var_cs_B = cs.create_str("B, C")
    var_cs_C = cs.create_str("B, C")

    print(cs.contains(var_cs_A, var_cs_B))
    print(cs.equals(var_cs_B, var_cs_C))

    print(cs.to_string(var_cs_A))
    print(cs.to_string(var_cs_B))

    return 0
# fim main

main()
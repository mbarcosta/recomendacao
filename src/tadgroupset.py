# -*- coding: utf-8 -*-

'''
 TAD Group set
 Versão 1.0
 01/03/2018
 .Ernani & Mateus

 Tipo abstrato de dados que representa um group set.
 Um groupset é uma coleção de choicesets.
 
 IMPORTANTE:
   Python 3.5 (casa) não aceita sobrecarga de métodos fora do modo O.O.
'''

import tadchoiceset as cs

'''
 Entradas: string choiceset, string operador, string choiceset. 
 Saida: um tad groupset   
'''
def create(str_lst_ofs_lado_equerdo, operador, str_lst_ofs_lado_direito):
    cs_esquerdo = cs.create_str(str_lst_ofs_lado_equerdo)
    cs_direito = cs.create_str(str_lst_ofs_lado_direito)
    return create(cs_esquerdo, operador, cs_direito)
## create

'''
 str_expressao_gs: 
      string contendo uma expressão groupset do tipo <choice set> <operador> <choiceset>.
      Protótipo, por enquanto.
'''
def create_exp(str_expressao_gs):
    '''
      Fazer um parsing do argumento de entrada e extrair uma expressão do tipo
      tadchoiceset (operando esquerdo) <operador> tadchoiceset (operando direito)
    '''
    return None
## create_str

def get_left(tad_gs):
    return tad_gs[0]
# get_left

def get_right(tad_gs):
    return tad_gs[2]
# get_right

def get_op(tad_gs):
    return tad_gs[1]
# get_op

'''
 Verifica se um determinado choice é um dos operandos de um groupset.
 
 Entradas: o groupset  
'''
def isoperand(tad_gs, tad_cs):
    return cs.equals(tad_cs, get_left(tad_gs)) or cs.equals(tad_cs, get_left(tad_gs))
## contido_cs

'''
  Verifica se o groupset é um membro do choiceset.
'''
def gs_in_cs(tad_gs, tad_cs):
    cs_esq = get_left(tad_gs)
    cs_dir = get_right(tad_gs)
    return cs.contains(tad_cs, cs_esq) and cs.contains(tad_cs, cs_dir)
# gs_in_cs
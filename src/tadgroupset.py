# -*- coding: utf-8 -*-

'''
 TAD Group set
 Versão 1.0
 Última alteração: 01/03/2018
 .Ernani & Mateus

 Tipo abstrato de dados que representa um group set.
 Um groupset é uma coleção de choicesets.
 
 IMPORTANTE:
   Python 3.5 (casa) não aceita sobrecarga de métodos fora do modo O.O.
   
   GitHub: https://github.com/mbarcosta/recomendacao
'''

import tadchoiceset as cs

'''
  Constrói um tad groupset a partir dos componentes (operandos e operadores) de uma expressão
  de criação de um groupset.
  
  Entradas: str_lst_ofs_lado_equerdo: string representando uma lista de objetos de fluxo usado como operando
  esquerdo da expressão definidora do groupset.
  str_lst_ofs_lado_direito: string representando uma lista de objetos de fluxo usado como operando
  direito da expressão definidora do groupset.
  
  Saida: um tad groupset. 
'''
def create(str_lst_ofs_lado_equerdo, operador, str_lst_ofs_lado_direito):
    cs_esquerdo = cs.create_str(str_lst_ofs_lado_equerdo)
    cs_direito = cs.create_str(str_lst_ofs_lado_direito)
    return [cs_esquerdo, operador, cs_direito]
## create

'''
  Constrói um tad groupset a partir de uma string contendo uma expressão de criação
  de um group set. Faz o parsing da string e usa os elementos para uma chamada ao
  constructor 'create' acima.  
  
  Entrada: str_expressao_gs: string contendo uma expressão de definição de groupset.
  Uma expressão que tem a forma <choice set> <operador> <choice set>.
  
  Saida: um tad groupset.
'''
def create_exp(str_expressao_gs):
    vet = str_expressao_gs.split()
    return create(vet[0], vet[1], vet[2])
## create_str

'''
  Retorna o operando esquerdo do tad groupset.
  
  Entrada: Um tad groupset qualquer.
  Saída: Um tad choiceset que faz o papel de operando esquerdo do groupset argumento de entrada.
'''
def get_left(tad_gs):
    return tad_gs[0]
# get_left

'''
  Retorna o operando direito do tad groupset.
  
  Entrada: Um tad groupset qualquer.
  Saída: Um tad choiceset que faz o papel de operando direito do groupset argumento de entrada.
'''
def get_right(tad_gs):
    return tad_gs[2]
# get_right

'''
  Retorna o operandor do tad groupset.
  
  Entrada: Um tad groupset qualquer.
  Saída: Uma string caracterizando o operador da expressão do groupset argumento de entrada.
'''
def get_op(tad_gs):
    return tad_gs[1]
# get_op

'''
 Verifica se um determinado choiceset é um dos operandos de um groupset. 
 
 Entradas: tad_gs, o groupset de interesse, tad_cs, o choiceset que pode ou não de um dos operandos de tad_gs.
 Saida: True, se tad_cs é um dos operandos de tad_gs, False caso contrário.  
'''
def isoperand(tad_gs, tad_cs):
    return cs.equals(tad_cs, get_left(tad_gs)) or cs.equals(tad_cs, get_left(tad_gs))
## contido_cs

'''
  Verifica se um determinado groupset é um dos membros do choice set.
  
  Entradas: tad_cs, o choiceset de interesse, tad_gs, o groupset que pode ou não de um dos operandos de tad_cs.
  Saida: True, se tad_gs é um dos operandos de tad_cs, False caso contrário.    
'''
def gs_in_cs(tad_gs, tad_cs):
    cs_esq = get_left(tad_gs)
    cs_dir = get_right(tad_gs)
    return cs.contains(tad_cs, cs_esq) and cs.contains(tad_cs, cs_dir)
# gs_in_cs
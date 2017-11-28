'''
 TAD Choice set
 Versão 1.0
 28/12/2017
 .Ernani

 Tipo abstrato de dados que representa um choice set.
 Inicialmente os objetos de fluxo serão representados como strings.

'''

'''
 Define e retorna a estrutura de dados que representa um choice set, cs.
 Um choice set é representado como uma lista de strings (objetos de fluco).
 
 Entrada: Uma lista de strings representando objetos de fluxo.
 Saida: uma lista de strings representado objetos de fluxo.
 
 Obs: revisões posteriores poderão redefinr o formato interno de um choce set
 para outra estrutura de dados diferente de listas. Contudo, a estrutura do
 parâmetro de entrada deverá permanecer. Ao menos enquanto o desenvolvimento
 mantiver um caráter exploratório.
 
 Glossário:
    cs: choiceset
    gs: groupset
    of: objeto de fluxo
'''
def create_cs(lst_str_ofs):
    return lst_str_ofs

'''
  Entradas: um tad choiceset, uma lista de objetos de fluxo a serem acrescentados ao tad.
  Saida: o tad choice set atualizado com os novos 
'''
def add_of(tad_cs, plst_ofs):
    return tad_cs + plst_ofs
## add_of

def to_string(tad_cs):
    saida = ""
    for of in tad_cs:
        saida = saida +", " + of
    return saida
## to_string




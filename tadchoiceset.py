#-*- coding: utf-8 -*-

'''
 TAD Choice set
 Versão 1.0
 28/12/2017
 .Ernani & Mateus

 Tipo abstrato de dados que representa um choice set.
 Inicialmente os objetos de fluxo serão representados como strings.
'''

'''
 Define e retorna a estrutura de dados que representa um choice set, cs.
 Um choiceset é representado como uma lista de strings (objetos de fluxo).
 Exemplo: ["A", "B", "C", etc.] onde "A", "B", "C" são objetos de fluxo (ofs).
 
 Entrada: Uma lista de strings representando objetos de fluxo.
 Saida: uma lista de strings representado objetos de fluxo.
 
 Obs: revisões posteriores poderão redefinr o formato interno de um choceset
 para outra estrutura de dados diferente de listas. Contudo, a estrutura do
 parâmetro de entrada deverá permanecer, pelo menos enquanto o desenvolvimento
 mantiver seu caráter exploratório.
 
 Glossário:
    of: objeto de fluxo
    cs: choiceset (uma coleção de objetos de fluxo)
    gs: groupset (uma coleção de choicesets)
    gst: groupset table (uma coleção de groupsets)    
'''
def create_cs(lst_str_ofs):
    return lst_str_ofs
## create_cs

'''
  Adiciona uma lista de novos objetos de fluxo ao conteúdo do tad_cs.
  Entradas: um tad choiceset, uma lista de objetos de fluxo a serem acrescentados ao tad.
  Saida: o tad choiceset atualizado com os novos objetos de fluxo.
'''
def add_of(tad_cs, plst_ofs):
    return tad_cs + plst_ofs
## add_of

'''
  Remove do conteúdo do tad_cs uma lista de objetos de fluxo.
  Entradas: um tad choiceset, uma lista de objetos de fluxo a serem removidos do conteúdo do tad.
  Saida: o tad choiceset atualizado sem os objetos de fluxo removidos.
'''
def remove_of(tad_cs, plst_ofs):
    for of in plst_ofs:
        if of in tad_cs:
            tad_cs.remove(of)
    return tad_cs
## remove_of

'''
  Testa se um choiceset está contido em outro choiceset.
  Entrada: choiceset que poderá ser um subconjunto do segundo choiceset,
           choiceset que poderá conter o primeiro choice set.
  Saida: True se o primeiro choiceset estiver todo incluído no segundo choiceset, False caso contrário.
'''
def contido_cs(tad_cs_A, tad_cs_B):
    for of in tad_cs_A:
        if of not in tad_cs_B:
            return False
    return True
## contido_cs

'''
  Testa a igualdade entre dois choicesets.
  Entrada: dois choicesets que terão seus conteúdos comparados.
  Saida: True se os conteúdos dos choicesets forem idênticos, False caso contrário.
'''
def igual_cs(tad_cs_A, tad_cs_B):
    return (len(tad_cs_A) == len(tad_cs_B)) and contido_cs(tad_cs_A, tad_cs_B)
## igual_cs

'''
  Testa se um determinado objeto de fluxo pertence ao choiceset.
  Entradas: um choiceset e um objeto de fluxo que pode ou não ser embro do choiceset.
  Saida: True se o objeto de fluxo é um membro do choiceset, False caso contrário.
'''
def pertence_of(tad_cs, pof):
    return pof in tad_cs
# pertence

'''
  Calcula e retorna o tamanho do choiceset (quantidade de objetos de fluxo).
  Entrada: um choiceset.
'''
def size_cs(tad_cs):
    return len(tad_cs)
## size_cs

'''
  Retorna o index-ésimo objeto de fluxo de um choiceset.
  Entradas: um choiceset e uma posição no choiceset.
  Saída: O objeto de fluxo residindo na index-ésima posição, se existir.
         Retorna None caso a posição especificada não exista no choiceset.
'''
def get_of(tad_cs, index):
    if index in range(len(tad_cs)):
        return tad_cs[index]
    else:
        return None
## get_of

'''
  Retorna uma string contendo os ids dos objetos de fluxo pertencentes ao tad choice set.
  Entrada: um tad choiceset
  Saida: uma string formata com os ids dos ofs separados por vírgula.
'''
def to_string(tad_cs):
    saida = ""
    for of in tad_cs:
        saida = saida +", " + of
    return saida[2:]
## to_string
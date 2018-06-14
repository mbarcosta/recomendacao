#-*- coding: utf-8 -*-

'''
 TAD Choice set
 Versão 1.0
 Última alteração: 28/12/2017
 .Ernani & Mateus
  GitHub: https://github.com/mbarcosta/recomendacao 

 Tipo abstrato de dados que representa um choice set.
 Um choiceset é uma coleção de objetos de fluxo, of.
 Inicialmente os objetos de fluxo serão representados como strings.
 etc..
'''
from posix import lstat

'''
 Define e retorna a estrutura de dados que representa um choice set, cs.
 Um choiceset é representado como uma lista de strings (objetos de fluxo).
 Exemplo: ["A", "B", "C", etc.] onde "A", "B", "C" são objetos de fluxo (ofs).
 
 Entrada: Uma lista de strings representando objetos de fluxo.
 Saida: uma lista de strings representando um choiceset.
 
 Obs: revisões posteriores poderão redefinr o formato interno de um choiceset
 para uma estrutura de dados diferente de listas.
 
 Glossário:
    of: objeto de fluxo
    cs: choiceset (uma coleção de objetos de fluxo)
    gs: groupset (uma coleção de choicesets)
    gst: groupset table (uma coleção de groupsets)    
'''
def create(lst_str_ofs):
    #
    # Futuramente aqui haverá a lógica que mapeará a lista de strings para
    # uma lista de objetos de fluxo.
    #
    return lst_str_ofs
## create_cs

'''
  Cria um tad choiceset a partir de uma string contendo os ids (labels) dos objetos de fluxo.
  Análogo a create.
  Entrada: uma string contendo os identificadores de objetos de fluxo (of) separados por vírgula.
           exemplo: "A, B, C, .."
  Saída: uma lista 
'''
def create_str(str_ofs):
    lst = str_ofs.split(",")    
    for i in range(len(lst)):
        lst[i] = lst[i].strip()
        
#     tup = tuple(lst)
#     lst.append(tup)
    return lst
# create_str

def add_contained_gs(cs, gs):
    if len(cs) == 1:
        cs.append([gs])
    else:
        cs[1].append(gs)
    return cs
# add_contained_gs

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
def remove(tad_cs, plst_ofs):
    for of in plst_ofs:
        if of in tad_cs:
            tad_cs.remove(of)
    return tad_cs
## remove_of

'''
  Faz o append, para o choiceset, de um novo objeto de fluxo.
  Entradas: um choiceset e um objeto de fluxo a ser acrescentado ao cs.
  Saída: o choiceset atualiza com o novo objeto de fluxo.
'''
def append(tad_cs, str_of):
    tad_cs.append(str_of)
    return tad_cs
## append

'''
  Testa se um choiceset está contém um outro choiceset.
  Entrada: choiceset que poderá conter um segundo choiceset,
           choiceset que poderá estar contido no primeiro choiceset.
  Saida: True se o primeiro choiceset contiver o segundo choiceset, False caso contrário.
'''
def contains(tad_cs_A, tad_cs_B):
    for of in tad_cs_B:
        if of not in tad_cs_A:
            return False
    return True
## contido_cs

'''
  Testa a igualdade entre dois choicesets.
  Entrada: dois choicesets que terão seus conteúdos comparados.
  Saida: True se os conteúdos dos choicesets forem idênticos, False caso contrário.
'''
def equals(tad_cs_A, tad_cs_B):
    return (len(tad_cs_A) == len(tad_cs_B)) and contains(tad_cs_A, tad_cs_B)
## igual_cs

'''
  Testa se um determinado objeto de fluxo pertence ao choiceset.
  Entradas: um choiceset e um objeto de fluxo que pode ou não ser membro do choiceset.
  Saida: True se o objeto de fluxo é um membro do choiceset, False caso contrário.
'''
def in_cs(tad_cs, pof):
    return pof in tad_cs
## in_cs

'''
  Calcula e retorna o tamanho do choiceset (quantidade de objetos de fluxo).
  Entrada: um choiceset.
'''
def size(tad_cs):
    return len(tad_cs)
## size_cs

'''
  Sinaliza se um choiceset está vazio ou não.
  Entrada: um tad choiceset.
  Saída: True se o choice não possui nenhum objeto de fluxo (of), False caso contrário.
'''
def isempty(tad_cs):
    return size(tad_cs) == 0
# isempty

'''
  Retorna o index-ésimo objeto de fluxo de um choiceset.
  Entradas: um choiceset e uma posição no choiceset.
  Saída: O objeto de fluxo residindo na index-ésima posição, se existir.
         Retorna None caso a posição especificada não exista no choiceset.
'''
def get_of_by_ndx(tad_cs, index):
    if index in range(len(tad_cs)):
        return tad_cs[index]
    else:
        return None
## get_of

'''
  Retorna o objeto de fluxo cujo id é passado como argumento.
  Entradas: um choiceset e um id de um objeto de fluxo.
  Saída: O objeto de fluxo com o id procurado, caso exista no choiceset. None 
         caso nenhum dos objetos de fluxo do choiceset possua o id procurado.
'''
def get_of_by_id(tad_cs, str_id):
    if str_id in tad_cs:
        return tad_cs[tad_cs.index(str_id)]
    else:
        return None
## get_of

'''
  Retorna uma string contendo os ids dos objetos de fluxo pertencente ao tad choice set.
  Entrada: um tad choiceset
  Saida: uma string formata com os ids dos ofs separados por vírgula.
'''
def to_string(tad_cs):
    saida = ""
    for of in tad_cs:
        saida = saida + ", " + of
    return saida[2:]
## to_string
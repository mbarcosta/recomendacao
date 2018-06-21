
'''
Tad GroupSetStack
GitHub: https://github.com/mbarcosta/recomendacao

Operações:
   Create
    Entrada: nil
    pós-condicao: objeto do tipo GroupSetStack é criado e configurado.
    Retorno: Referência para um tipo GroupSetStack novo, vazio

   InsertGroupSet
      entrada: situação do tipo escolha.
      insere o groupSet corresponde à situação no GroupSetStack respeitando a estrutura de pertinência.
      
   RemoveGroupSet
       Remove o grouSet mais externo (do topo da GroupSetStack)
'''

import tadchoiceset as tadcs
import tadgroupset as tadgs

'''
  Cria um tad group set table vazio, sem nenhum group set cadastrado.
  Saída: uma lista 
'''
def create():
    return []
# create

'''
  Adiciona um group set a um group set table.
  Entrada: tadGSTab (tad group set table) que conterá o group set adicionado.
           gs: group set a ser adicionado na tabela tadGSTab.
   Saída: retorna o tad group set table tadGSTab alterado com mais 1 group set.
'''
def addGS(tadGSTab, gs):
    if tadGSTab == []:
        tadGSTab.append([gs])
    else:
        for indexNivel, nivel in enumerate(tadGSTab):
            for elemGS in nivel:
                # Verificando a inserção:
                # a) verifica-se se o group set a ser inserido, gs, está
                #    interiramente contido em um choice set de algum group set
                #    que já existe em tadGSTab.
                cs_esq = tadgs.get_left(elemGS)
                cs_dir = tadgs.get_right(elemGS)
                
                if tadgs.gs_in_cs(gs, cs_esq) or tadgs.gs_in_cs(gs, cs_dir):
                    # Inserir gs em um nível abaixo da tabela.
                    # Nível mais alto como sendo zero, e descendo a partir daí.
                    if indexNivel + 1 < len(tadGSTab):
                        tadGSTab[indexNivel + 1].append(gs)
                    else:
                        tadGSTab.append([gs])
                        
                    if tadgs.gs_in_cs(gs, cs_esq):                      
                        tadgs.add_cs_container(gs, cs_esq)
                        tadcs.add_contained_gs(cs_esq, gs)
                        
                    elif tadgs.gs_in_cs(gs, cs_dir):                       
                        tadgs.add_cs_container(gs, cs_dir)
                        tadcs.add_contained_gs(cs_dir, gs)
                    
                    break
            # for elemGS in enumerate(nivel)..
        # for indexNivel, nivel in ..
        
        # Insere gs no topo da tabela, nível zero.
        tadGSTab[0].append(gs)
    # else ..
    
    return tadGSTab
# addGS

def printTabGS(tadGSTab):    
    #-------------------------------------- for i, nivel in enumerate(tadGSTab):
        #--------------------------------------- print("Nivel:", i, " [",end="")
        #----------------------------------------- for j in range(len(nivel)-1):
            #--------------------- print(tadgs.to_string(nivel[j]), ",", end="")
        #----------------------------- print(tadgs.to_string(nivel[-1]), end="")
        #------------------------------------------------------------- # for j..
        #---------------------------------------------------- print("]", end="")
        #--------------------------------------------------------------- print()
        #------------------------------------------------------- print("-" * 90)
    #----------------------------------------------------------------- # for i..
    print(len(tadGSTab), "níveis")
    for l in range(len(tadGSTab)):
        print("Nivel",l," --> ",tadGSTab[l])
    print(tadGSTab)
# printTabGS

'''
  Remove um group set de um group set table.
  Entrada: tadGSTab (tad group set table) que contem o group set a ser removido.
           gs: group set a ser removido da tabela tadGSTab.
  Saída: retorna o tad group set table tadGSTab sem o group set removido (gs).
         Caso o gs não exista, retorna o group set table inalterado.
'''
def removeGS(tadGSTab, gs):
    # EM OBRAS
    return tadGSTab
# removeGS

'''
  Remove um group set de um group set table.
  Entrada: tadGSTab (tad group set table) que contem o group set a ser removido.
           gs: group set a ser removido da tabela tadGSTab.
  Saída: retorna o tad group set table tadGSTab sem o group set removido (gs).
         Caso o gs não exista, retorna o group set table inalterado.
'''
def findGS(tadGSTab, idGS):
    # EM OBRAS
    return None











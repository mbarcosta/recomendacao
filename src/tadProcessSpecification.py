""" implementação do tipo abstrato de dados ProcessSpecification
Operações
- insertAfo - insere um objeto de fluxo no domínio da especificação - checa duplicidade, checa sintaxe do nome do afo permitindo somente alfanumericos iniciado por letra
- insertAfoSet - insere um grupo de objetos de fluxo no domínio da especificação - usa a operação insertAfo
- insertSituation - insere uma situação no conjunto de situações da especificação.
- getChoiceRelationsGroup - obtem o conjunto de situações que são relações de escolha: São as relações baseadas em não coexistência (xor) e união (or). retorna um conjunto de situações. o conjunto de choice relations
será usado para montar o groupSet inicial do processo.
- getIndependentSet - obter o conjunto de afos que não estão em uma situação ativa de dependência como <<dependers>> nem que estão numa situação ativa de escolha. - Retorna um conjunto  de afos.
O conjunto de afos independentes vai ser usado para para gerar recomendações. O termo ativa significa que a situação ainda não foi satisfeita pelo modelo (ainda não foi utilizada).
- getDomain - retorna o conjunto de afos completo da especificação
- getSituationsSet - retorna o conjunto completo de situações da especificação.
- o separador entre as situações é o caractere |
"""
def create(str_lst_ofs, str_lst_situations):
        return [str_lst_ofs, str_lst_situations]

def insertAfo(tadPS, afo):
    return ([tadPS[0]+","+afo,tadPS[1]])
def insertSituation(tadPS, situation):
    return ([tadPS[0],tadPS[1]+"|"+situation])
def getDomain(tadPS):
    return (tadPS[0])
def getSituationSet(tadPS):
    return tadPS[1]
def getChoiceRelationsGroup(tadPS):
    situations = tadPS[1].split("|")
    for index, item in enumerate (situations):
        if (("xor" in item) or ("or" in item)):
            print(index, "-" ,item)


def main():
    p1 = create("a,b,c","a xor b")
    p1 =insertAfo(p1,"d")
    p1 = insertSituation(p1,"c or d")
    p1 = insertSituation(p1, "c dep d")
    print(p1)
    print("imprimindo as choice relations:\n")
    getChoiceRelationsGroup(p1)
main()

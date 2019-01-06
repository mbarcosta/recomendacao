""" implementação do tipo abstrato de dados ProcessSpecification
Operações
- insertAfo - insere um objeto de fluxo no domínio da especificação - checa duplicidade, checa sintaxe do nome do afo permiinfo somente alfanumericos iniciado por letra
- insertAfoSet - insere um grupo de objetos de fluxo no domínio da especificação - usa a operação insertAfo
- insertSituation - insere uma situação no conjunto de situações da especificação.
- getChoiceRelationsGroup - obtem o conjunto de situações que são relações de escolha: São as relações baseadas em não coexistência (xor) e união (or). retorna um conjunto de situações
- getIndependentSet - obter o conjunto de afos que não estão em uma situação ativa de dependência como <<dependers>> nem que estão numa situação ativa de escolha. - Retorna um conjunto  de afos.
O conjunto de afos independentes vai ser usado para para gerar recomendações. O termo ativa significa que a situação ainda não foi satisfeita pelo modelo (ainda não foi utilizada).
- getDomain - retorna o conjunto de afos completo da especificação
- getSituationsSet - retorna o conjunto completo de situações da especificação.
"""


def main():
    print("Vamos lá de novo")
main()
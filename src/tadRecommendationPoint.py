""" Um ponto de recomendação é uma posição no modelo onde recomendações podem ser inseridas
Ele é determinante na geração de recomendações.
O conjunto de todos os pontos de recomendação gerados atravéz da geração interativa de recomendações forma um grafo cujos nõs são pontos de recomendações e as arestas
conectam os pontos na ordem em que evoluem as recomendações
Um estado do modelo pode conter zero ou mais pontos de recomendação. Um ponto de recomendação possui os seguintes atributos:
 Domain: D - cada ponto de recomendação vai possuir um domínio específico
    - ExecutionState- o execution state é o estado de execução que  o processo chega ao atingir o ponto de recomendação. Ele serve para verificar quais os afos já foram executados até então,
    permitindo checar se dependências foram satisfeitas..
     Sua representação é um vetor binário de tamanho igual numero de elementos do Domínio do processo. NO vetor um bit 0 siginifica que o afo não foi executado naquele ponto. Um bit 1 significa que o afo
     foi executado ao aintigir aquele ponto.
    - Independent Set - oConjunto independente é obtido a partir do domínio, (veja no tadProcessSpecification, como ele é obtido)
    - groupSetTable: gst - Gerada a partir da operação getChoiceRelationsGroup do ProcessSpecification do estado que contém o ponto de recomendação
    - Parent Recommendation point é um ponteiro para o ponto de recomendação anterior que o  gerou
    - NextRecommendationPOints[] - Vetor apontando para o próximo pontos de recomendação gerados a partir de uma recomendação tomada a partir do ponto de recomendação em questão.
    bla bla bla
"""
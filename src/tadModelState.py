""" Este tad tem a função de representar o estado atual da modelagem, tanto com relação a sua estrutura quanto com relação às estruturas usadas para a recomendação (recommendation point)
O processo de modelagem será representado ao final por uma lista encadeada de estados de modelo que levam de um estado com um  modelo vazio para um estado com um modelo
que não viole nenhuma situação e que inclua todos os afos da especificação.
Os atributo do estado do modelo são:
 - the current process model described in a meta-model language used by recommendations
 - a stack with the taken recommendations used to reach the state
 - a pointer to its previous state
 - a pointer to its next state - Note that there is only one next state since only one recommendation can be taken. The recommendation at the stack top is the one that makes a transition to the next state
 - a pointer for each state's recommendation point

 - as operações do tadModelState são os getters e setters de todos os seu atributos.


"""
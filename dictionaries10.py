# 10) Crie um conjunto usando as duas sintaxes diferentes para criar um conjunto.
mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print("\nmySet:", mySet)
print("mySet2:", mySet2)

# Resposta: Qual é a diferença? Importa como você cria o conjunto?
print("\nA diferença entre os dois é a forma como os elementos são adicionados. No primeiro caso (set()), "
      "cada caractere da string é adicionado como um elemento individual. No segundo caso ({}), a string completa é "
      "adicionada como um único elemento. Sim, importa como você cria o conjunto, pois pode alterar seus elementos e "
      "sua estrutura.")



# 11) Encontre a interseção, diferença, união e diferença simétrica entre os dois conjuntos.
setA = {3, 14, 15, 9, 26, 5, 35, 9}
setB = {60, 22, 14, 0, 9}

print("Interseção de A e B:", setA.intersection(setB))
print("Diferença de A para B:", setA.difference(setB))
print("União de A e B:", setA.union(setB))
print("Diferença simétrica entre A e B:", setA.symmetric_difference(setB))

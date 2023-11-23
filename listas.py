"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321

# string = 'ABCDE' # 5 caracters (len)
# lista = [123,True,'JoseFabio',1.2,[]] # com se fosse uma lista vazia
# lista[2] = 'Jose Fabio'
# print(bool({}))
# print(lista,type(lista))

lista = [10,20,30,40]
lista[2] = 300




# del lista[2] # apagar indice 2 da lista

# print(lista)
# print(lista[2],type(lista[2]))

lista.append(50)    # adicionar mais itens a lista.
lista.pop()     # Remove o último elemento.
lista.append(60)
lista.append(70)
lista.append(80)
lista.pop()     #  sempre remove o ultimo item da lista
print(lista)

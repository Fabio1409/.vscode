"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# lista_a = ['JoseFabio','Patricia','Miguel']
# lista_b = lista_a.copy()    # retona a lista_a

# lista_a[0] = 'Qualquer coisa'   # se mudar uma variavel mudas as outras copiadas tbm,lista matavel.
# print(lista_a)
# print(lista_b)

'''
for in com listas
'''

lista = ['Maria','João','Pedro','Fabio']
lista.append('JoseFabio')
indices = range(len(lista))

for indice in indices:
   
    print(indice,lista[indice],type(lista[indice]))
   
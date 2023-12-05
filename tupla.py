'''
Introdução ao desempacotamento + tuplas(tuplas)

'''
# nomes = ['maria','Helena','JoseFabio']
# nome1,nome2,nome3 = nomes
# print(nome3)
#  DESEMPACOTAMENTO.
# _,_,nome,*resto = ['maria','Helena','Josefabio']
# print(nome,resto)

# TUPLAS
nome = ['Maria','Helena','Fabio']
nome.append('Miguel')
#nome = list(nome)   # TRANSFORMANDO TUPLA EM  LISTA
#nome = tuple(nome)  # TRANSFORMANDO LISTA EM TUPLA
for item in enumerate(nome):
    a,b = item
    print(a,b)

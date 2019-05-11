
# revisao rapida
# escrever uma função que recebe
# um numero inteiro e retorna uma lista
# com todos os números menores ou iguais a esse
# menos o zero
# ex: gerar_lista(5) -> [1,2,3,4,5]


#1
# def gerar_lista(n):
#	lista, x = [], 1
#	while x <= numero:
#		lista.append(x)
#		x += 1
#	return lista

#2
#def gerar_lista(n):
#	lista = []
#	for i in range(n):
#		lista.append(i + 1)
#	return lista

#3
#def gerar_lista(n):
#	return [i + 1 for i in range(n)]

#4
#gerar_lista = lambda n: [i + 1 for i in range(n)]

def par(x):
	if x % 2 == 0:
		return True
	return False

def gerar_lista_par(n):
	return [i + 1 for i in range(n) if par(i + 1)]

lista_de_numero_par = gerar_lista_par(5)
for n in lista_de_numero_par:
	if not par(n):
		raise Exception('{} não é um numero par'.format(n))

print (lista_de_numero_par)
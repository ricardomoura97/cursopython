
import json

import aleatorio as foo

def imprimir_bonito(obj):
	print(json.dumps(obj, indent=2))

def gerar_lista_usuarios(n):
	lista = []
	for i in range(n):
		u = foo.gerar_usuario_aleatorio()
		lista.append(u)
	return lista


lista_de_usuarios = gerar_lista_usuarios(100)

for usuario in lista_de_usuarios:
	print('idade: {}'.format(usuario['idade']))
	if usuario ['idade'] > 30:
		imprimir_bonito(usuario)


def gerar_csv(lista):
	TEMPLATE = '{};{};{};'
	cabecalho = TEMPLATE.format('NOME','EMAIL','IDADE')
	for usuario in lista:
		usuario_formatado = TEMPLATE.format(
			usuario['nome'],
			usuario['email'],
			usuario['idade']
		)
		print(usuario_formatado)

def filtrar_usuarios(usuario):
	usuario_email = usuario['email'].lower()
	if 'd' in usuario_email or 'a' in usuario_email:
		return True
	return False
	
gerar_csv(u for u in lista_de_usuarios if filtrar_usuarios(u))	
lista_de_gatos = [ 
	{
	 'nome' : 'gato',
	 'peso' : 5000,
	 'idade': 6,
	 'apelido': 'sedoso',	 
	}, 
	{
	 'nome': 'ferando',
	 'peso': 3750,
	 'idade': 3,
	 'apelido': 'brilhoso'
	}
]
'''
def get_input_as_int(mensagem):
	user_input = input(mensagem)
	for token in user_input:
		print('Caracter atual: {}'.format(token))
		if token not in '0123456789':
			print('Caracter invalido encontrado')
			print('Encerrando o algoritmo com erro')
			#encerrando o algoritmo
			return -1
	print('Algoritmo executado com sucesso!')
	return int(user_input)
	#solução nutela
	#if user_input.isdigit():
	#return int(user_input)
get_input_as_int('Caso de teste: ')
'''

#contexto do erro

def get_input_as_int(mensagem,erro):
	user_input = input(mensagem)
	try:
		return int(user_input)
	except ValueError:
		raise ValueError(erro)

#tratamento do erro

def tratamento_de_tentativa(numero_tentativas, mensagem, erro):
	for tentativa in range(numero_tentativas):
		try:
			return get_input_as_int(mensagem,erro)
		except ValueError as err:
			restantes = numero_tentativas - (tentativa + 1)
			print('Um erro aconteceu, você ainda tem {} chances'.format(restantes))	
			print(err)
		print('Voce erro o input {} vezes.'.format(numero_tentativas))
		print('Vou encerrar o programa')
		exit()

novo_gato = {
	'nome' : input('Digite o nome de seu gato: '),
	'peso' : tratamento_de_tentativa(
		5, 'Digite o Peso: ', 'O peso deve ser um número maior que 0'
		),
	'idade': tratamento_de_tentativa(
		3, 'Digite a idade: ', 'A idade deve ser um número maior que 10'
		),
	'apelido': input('Digite o apelido do gato: ')
	
}
lista_de_gatos.append(novo_gato)

for gato in lista_de_gatos:
	print('Peso do gato: {}'.format(gato['peso']))
	if gato ['peso'] > 4000:
		print('Esse é o gato')
	else:
		print('Ela é a Malawi')
exit()
print("hello, world")

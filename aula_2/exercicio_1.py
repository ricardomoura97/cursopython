import datetime

def cadastrar_usuario():

	novo_usuario = {
		'data_do_cadastro': datetime.datetime.now(),
		'nome': input('Digite seu nome: '),
        'idade': input('Digite sua idade: '),
        'endereço': input('Digite seu endereço: '),
        'email': input('Digite seu email: '),
        'sexo' : input('Digite seu sexo: ')

    }
    
	return novo_usuario

novo_usuario = cadastrar_usuario()
print(novo_usuario)

d = novo_usuario['data_do_cadastro']
print(d.strftime('São Paulo, %d de %B de %Y))

'''
probabilidade = random.random()
if probabilidade < 0.8:
	cadastrar_usuario()
else:
	print('Opa, não deu sorte...')
exit()

#uma das utilidades do módulo random
#não esquecer de importar nas primeiras linhas do código
'''
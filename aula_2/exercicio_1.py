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
print(d.strftime('%B %d,%Y'))

#como cadastrar um usúario no mongo



import pymongo

client = pymongo.MongoClient()

db = client.projeto

def extrair_usuarios():
	return list (db.users.find())

def cadastra_usuario(nome, email, idade):

	usuario = db.users.find_one({ 'email': email })  # checagem se há o email no banco de dados já
	if not usuario:									 # se não houver o email pode criar
		db.users.insert({
		'nome' : nome,
		'email' : email,
		'idade' : idade
	})

cadastra_usuario(
	'Ricardo Moura Caires Costa',
	'ricardo.moura@gmail',
	21
)

for usuario in extrair_usuarios():
	print (usuario)


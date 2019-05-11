#Orientação a objeto

class User:

	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age

name = input('Digite seu nome: ')
email = input('Digite seu email: ')
age = int(input('Digite sua idade: '))

user = User(name, email, age)

if age >= 18:
	print('Permitido')
	
else:
	print('Não permitido')

	pass


class Cadastrador:

	def cadastrar_usuario(self):
		name = input('Digite seu nome: ')
		email = input('Digite seu email: ')
		age = int(input('Digite sua idade: '))
		
		return User(name, email, age)

cadastrador = Cadastrador()

user = cadastrador.cadastrar_usuario()

if user.age >= 18:
	print('Permitido')
	
else:
	print('Não permitido')

	pass


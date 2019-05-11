
import datetime


''' 
Quando o usuário passar um ticket válido na catraca
a catraca deve liberar e o preço da passagem deve ser
descontado do saldo do ticket. Um ticket válido é um 
ticket que está dentro do prazo de validade, tem saldo
suficiente para pagar a passagem e pertence à mesma 
concessionária do ônibus
'''

##########################################################################################
#Constantes
##########################################################################################

PRECO_DA_PASSAGEM = 4.00

##########################################################################################
#Erros
##########################################################################################


class ErroTicketExpirado(Exception):
	pass

class ErroTicketSemSaldo(Exception):
	pass

class ErroTicketOutraConcessionaria(Exception):
	pass

##########################################################################################
#Classes
##########################################################################################

class Ticket:

	def __init__(self, validade, saldo, concessionaria):
		
		self.validade = validade
		self.saldo = saldo
		self.concessionaria = concessionaria

	def descontar(self, saldo):

		self.saldo = self.saldo - saldo

class Catraca:

	def __init__(self, concessionaria):
		
		self.estado = 'travada'
		self.concessionaria = concessionaria
	
	def esta_liberada(self):
		
		if self.estado == 'liberada':
			return True
		return False

	def descontar(self, valor):
		
		self.saldo = self.saldo - valor

	def	liberar(self, ticket):
		
		if ticket.concessionaria != self.concessionaria:
			raise ErroTicketOutraConcessionaria

		if ticket.saldo < PRECO_DA_PASSAGEM:
			raise ErroTicketSemSaldo

		if ticket.validade < datetime.datetime.now():
			raise ErroTicketExpirado

		self.estado = 'liberada'
		ticket.descontar(PRECO_DA_PASSAGEM)
	
if __name__ == '__main__':

##########################################################################################
#Testes
##########################################################################################

#Teste de Concessionaria do Ticket

	try:

		validade = datetime.datetime.now() + datetime.timedelta(days=2)
		saldo = PRECO_DA_PASSAGEM + 1
		concessionaria = 'sptrans'

		ticket = Ticket(validade, saldo, concessionaria)

		catraca = Catraca(concessionaria='emtu')

		catraca.liberar(ticket)

	except ErroTicketOutraConcessionaria:
		print('Teste concessionaria ok')

	#Teste de saldo do ticket

	try:

		validade = datetime.datetime.now() + datetime.timedelta(days=2)
		saldo = PRECO_DA_PASSAGEM - 1.00
		concessionaria = 'sptrans'

		ticket = Ticket(validade, saldo, concessionaria)

		catraca = Catraca(concessionaria='sptrans')

		catraca.liberar(ticket)

	except ErroTicketSemSaldo:
		print('Teste de saldo ok')


	#Teste de validade do ticket

	try:

		validade = datetime.datetime.now() - datetime.timedelta(days=2)
		saldo = PRECO_DA_PASSAGEM + 1
		concessionaria = 'sptrans'

		ticket = Ticket(validade, saldo, concessionaria)

		catraca = Catraca(concessionaria='sptrans')

		catraca.liberar(ticket)

	except ErroTicketExpirado:
		print('Teste de ticket expirado ok')

	#Teste de Catraca liberada

	validade = datetime.datetime.now() + datetime.timedelta(days=2)
	saldo = PRECO_DA_PASSAGEM + 1
	concessionaria = 'sptrans'

	ticket = Ticket(validade, saldo, concessionaria)

	catraca = Catraca(concessionaria='sptrans')

	catraca.liberar(ticket)

	try:

		assert ticket.saldo == (saldo - PRECO_DA_PASSAGEM)
		assert catraca.esta_liberada()

		print('teste de fluxo feliz ok')

	except:
		print('BUG ENCONTRADO')
		
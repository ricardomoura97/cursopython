
import datetime
import unittest

import exercicio_1 as scooby

class CatracaTeste(unittest.TestCase):

	def test_ticket_vencido(self):

		validade = datetime.datetime.now() - datetime.timedelta(days=2)
		saldo = scooby.PRECO_DA_PASSAGEM + 1
		concessionaria = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, concessionaria)

		catraca = scooby.Catraca(concessionaria='sptrans')

		with self.assertRaises(scooby.ErroTicketExpirado):
			catraca.liberar(ticket)
		
	def test_saldo_insuficiente(self):


		validade = datetime.datetime.now() + datetime.timedelta(days=2)
		saldo = scooby.PRECO_DA_PASSAGEM - 1.00
		concessionaria = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, concessionaria)

		catraca = scooby.Catraca(concessionaria='sptrans')

		with self.assertRaises(scooby.ErroTicketSemSaldo):
			catraca.liberar(ticket)

	def test_concessionaria_ticket(self):


		validade = datetime.datetime.now() + datetime.timedelta(days=2)
		saldo = scooby.PRECO_DA_PASSAGEM + 1
		concessionaria = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, concessionaria)

		catraca = scooby.Catraca(concessionaria='emtu')

		with self.assertRaises(scooby.ErroTicketOutraConcessionaria):
			catraca.liberar(ticket)

	def test_fluxofeliz(self):
		
		validade = datetime.datetime.now() + datetime.timedelta(days=2)
		saldo = scooby.PRECO_DA_PASSAGEM + 1
		concessionaria = 'sptrans'

		ticket = scooby.Ticket(validade, saldo, concessionaria)

		catraca = scooby.Catraca(concessionaria='sptrans')

		catraca.liberar(ticket)


		self.assertTrue(ticket.saldo == (saldo - scooby.PRECO_DA_PASSAGEM))
		self.assertTrue(catraca.esta_liberada())

if __name__ == '__main__':
	unittest.main()

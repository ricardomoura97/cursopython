
import threading

from modules import banco


if __name__ == '__main__':

	try:
		thread = threading.Thread(target=banco.ler_mensagens)
		thread.start()
	except Exception as err:
		print('Falha ao criar thread: {}'.format(err))
		exit()

	nome = input('Digite seu nome: ')
	while True:
		mensagem = input('Digite sua mensagem: ')
		banco.cadastrar_mensagem(nome, mensagem)
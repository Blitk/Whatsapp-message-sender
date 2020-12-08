from pyautogui import click, press, size, hotkey
import webbrowser as web
from time import sleep
from os import getcwd, path, chdir
from csv import DictReader


class Whats_Bot:
	primeiro = True

	def __init__(self):
		self.Contatos = self.carregar()
		self.mensagem = ""


	@staticmethod
	def carregar():
		chdir("contatos")
		lista_contatos = []

		with open("contatos.csv") as arquivo:
			leitor = DictReader(arquivo)
			for contato in leitor:
				lista_contatos.append(contato)

		chdir("..")
		return lista_contatos


	def enviar(self):
		for contato in self.Contatos:
			self.mensagem = f"Olá {contato['nome']}, Tudo bem com você?"
			sleep(4)
			web.open("https://web.whatsapp.com/send?phone="+contato["telefone"]+"&text="+self.mensagem)
			if Whats_Bot.primeiro:
				sleep(8)
				Whats_Bot.primeiro = False
			width, height = size()
			click(width/2, height/2)
			sleep(6)
			press('enter')
			sleep(6)
			hotkey('ctrl', 'w')
			

enviar_mensagens = Whats_Bot()
enviar_mensagens.carregar()
enviar_mensagens.enviar()
		
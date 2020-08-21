# gestion du systeme de fichiers
class dir():
	
	def dir_maker():
		import os
		try:
			os.mkdir('virtual/')
			os.mkdir('virtual/system')
			os.mkdir('virtual/receved')
			os.mkdir('virtual/sended')
		except FileExistsError:
			pass
if __name__ == '__main__':
	pass
	
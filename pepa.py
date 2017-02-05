class Animal(object):
	pass

	def quien_soy(self, vivo):
		print "Soy un animal"
		self.vivo = vivo
		if int(self.vivo) == 1:
			print "Estoy vivo"
		elif int(self.vivo) == 0:
			print "Estoy muerto"
		else:
			print "No se que estoy"

		return "Que lindo"

class Dog(Animal):

	def __init__(self, name):
		self.name = name


class Pescao(object):

	def __init__(self):
		self.quien = "Soy un pescao"

class Salmon(Pescao):

	def __init__(self):
		super(Salmon, self).__init__()
		self.estado = "Soy un salmon"

class SalmonAhumado(Salmon):

	def __init__(self):
		super(SalmonAhumado, self).__init__()

# Override explicitely
class Parent(object):

	def override(self):
		print "PARENT override()"


class Child(Parent):

	def override(self):
		print "CHILD override()"
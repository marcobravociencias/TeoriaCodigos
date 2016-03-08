##Clase de polinomios
import numpy as np
import math as mt
class polinomio(object):
	def __init__(self,coeficientes):
		super(polinomio, self).__init__()
		self.coeficientes=coeficientes
		sel.grado=coeficientes.size

	def es_irreducible(self):
		if self.grado>7:
			return True
		return False
	def suma(self,polin):

		if self.size <=polin.size:
			menor=self
			mayor=polin
		else:
			menor=polin
			mayor=self

		acarreo= mt.fabs(self.size-menor.size)
		menor_ext=np.array([])
		for x in acarreo:
			menor_ext=np.append(menor_ext,0)
		return np.array(menor_ext+mayor)
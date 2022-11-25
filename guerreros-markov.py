import pandas as pd
import numpy as np

def crear_matriz(n: int):
	"""Crea matriz estocastica para tamaño n"""
	# Inicializar a DataFrame vacio
	grupos = [i + 1 for i in range(n)]
	df = pd.DataFrame(columns=grupos, index=grupos)

	# Poblar DataFrame con numeros aleatorios que suman 1 y diagonal en 0
	for grupo in grupos:
		r = np.random.rand(n - 1)		#	Arreglo aleatorio de tamaño n-1
		probabilidades = r/r.sum()	#	Se divide entre la suma del arreglo para que su suma sea 1
		df.loc[grupo] = np.insert(probabilidades, grupo-1, 0)	#	Se inserta en el DataFrame con 0 en la posicion grupo - 1

	return df

def actualizar_matriz():
	"""Actualiza matriz y elimina un grupo"""
	return

def guerreros_markov():
	"""Correr codigo"""
	return

if __name__ == "__main__":
	print(crear_matriz(10))
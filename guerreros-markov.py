import pandas as pd
import numpy as np

def crear_matriz(n: int = 3, grupos: list = None):
	"""Crea matriz estocastica con diagonal en 0 para tamaño n"""
	# Inicializar a DataFrame vacio
	if not grupos:
		print("Matriz estocastica INICIAL:")
		grupos = [i + 1 for i in range(n)]
	df = pd.DataFrame(columns=grupos, index=grupos)

	# Poblar DataFrame con numeros aleatorios que suman 1 y diagonal en 0
	i = 0
	for grupo in grupos:
		r = np.random.rand(len(grupos) - 1)		#	Arreglo aleatorio de tamaño grupos-1
		probabilidades = r/r.sum()	#	Se divide entre la suma del arreglo para que su suma sea 1
		df.loc[grupo] = np.insert(probabilidades, i, 0)	#	Se inserta en el DataFrame con 0 en la diagonal
		i += 1

	print(df)
	print("=" * (10 * len(grupos) + 2))
	return df

def eliminar_grupo(df: pd.DataFrame, grupo_eliminado: int):
	"""Elimina fila y columna de grupo"""
	# Borrar fila y columna
	df = df.drop(labels=grupo_eliminado)
	df = df.drop(columns=grupo_eliminado)

	# Se vuelve a crear la matriz con los grupos restantes
	print("Reconfigurando matriz estocastica")
	df = crear_matriz(grupos = list(df.columns))
	return df

def guerreros_markov():
	"""Correr codigo"""
	return

if __name__ == "__main__":
	df = crear_matriz(n=4)
	print(eliminar_grupo(df, 2))
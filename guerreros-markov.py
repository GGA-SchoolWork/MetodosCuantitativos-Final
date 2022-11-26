import pandas as pd
import numpy as np
import argparse
import random

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
	print()
	return df

def eliminar_grupo(df: pd.DataFrame, grupo_eliminado: int):
	"""Elimina fila y columna de grupo"""
	# Borrar fila y columna
	df = df.drop(labels=grupo_eliminado)
	df = df.drop(columns=grupo_eliminado)

	# Se vuelve a crear la matriz con los grupos restantes
	print("NUEVA matriz estocastica:")
	df = crear_matriz(grupos = list(df.columns))

	return df

def mostrar_grupos(guerreros: dict):
	"""Muestra los grupos y sus guerreros"""
	print("Grupos y sus guerreros:")
	for grupo in guerreros:
		if guerreros[grupo]:
			print(f"Grupo {grupo}:\t{guerreros[grupo]}")
	print("=========================\n")

def guerreros_markov(n: int):
	"""Correr codigo"""
	if n == None:
		n = 3

	# Crear matriz inicial
	df = crear_matriz(n)

	# Diccionario con numero de guerreros en cada grupo
	guerreros = {}
	for i in range(1,n+1):
		guerreros[i] = random.randint(1,100)
	
	mostrar_grupos(guerreros)

	while len(df.columns) != 1:
		atacante = random.choice(df.columns)	# Escoger aleatoriamente quien ataca
		probabilidades = df.loc[[atacante]].values.flatten().tolist()	# Convertir fila de DataFrame a lista
		victima = np.random.choice(df.columns, p=probabilidades)			# Escoger victima de lista con probabilidades
		guerreros[victima] -= 1

		print(f"Grupo {atacante} ataca al grupo {victima}")
		mostrar_grupos(guerreros)
		
		# El grupo quedo sin guerreros
		if guerreros[victima] == 0:
			print(f"El grupo {victima} ha sido eliminado!")
			df = eliminar_grupo(df, victima)

		# Solo queda un grupo
		if len(df.columns) == 1:
			print("==========================")
			print(f"El grupo {atacante} es el ganador!")
			print("==========================")
			return

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Simular una batalla de diferentes grupos de guerreros con cadenas de Markov")
	parser.add_argument("--n", dest="n", type=int, help="Numero de grupos a luchar")
	args = parser.parse_args()
	
	if args.n and args.n < 2:
		raise Exception("Deben haber minimo 2 grupos.")
	
	guerreros_markov(n = args.n)
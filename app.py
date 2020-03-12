from myutils.kit import Board
from random import randint, random
import copy
from math import e
import matplotlib.pyplot as plt 
import numpy as np

# inicializacion de variables globales
numNeighbours = 16
results = np.zeros((100, 10)) #m matriz de resultados
solutions:[Board] = [] 

for run in range(0, 10): # corre el algoritmo 10 veces para graficar resultados
    found_solution = False
    while True: # Correr hasta encontrar solución
        T = 32 # inicializar T (arbitrario), 4 veces la cantidad de reinas
        bestBoard = Board() 
        bestScore = bestBoard.score
        if found_solution: 
            break
        for iteration in range(100): # 100 iteraciones por corridas
            if found_solution: 
                break
            neighbours = [copy.deepcopy(bestBoard).permutate() for n in range(numNeighbours)]
            for n in neighbours: 
                newScore = n.score
                if newScore <= bestScore:  # menor o igual porque no affecta y para que explore mas possibilidades
                    bestBoard = n
                    bestScore = newScore
                elif bestBoard.score == 0: 
                    found_solution = True
                    solutions.append(bestBoard) # guarda la solucion
                    break
                else: # calcula la probabildad para minimizar
                    delta = (bestBoard.score - n.score)
                    coefi = delta/T
                    randval = random()
                    transitionFunc = e**coefi  # e ^ coeficiente
                    if randval < transitionFunc: 
                        bestBoard = n
                        bestScore = newScore
            T *= 0.90 # reduel a temperatura 
            results[iteration, run] = bestScore

averages = np.average(results, 1).reshape(100, 1)
deviations = np.std(results, 1).reshape(100, 1)
dMinusAverages = averages - deviations # promedio menos la desviacion
dPlusAverages = averages + deviations # promedio mas la desviacion 

#graficar los datos
plt.plot(range(100), dMinusAverages)
plt.plot(range(100), averages)
plt.plot(range(100), dPlusAverages)
plt.show() 

# despliega las soluciones guardadas
for solution in solutions: 
    print(solution)



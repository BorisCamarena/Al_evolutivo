#Algoritmo genetico
# ( Maximo de la funcion ).

# Importamos librerias.

import matplotlib.pyplot as plt
import numpy as np 
import math 

# Implementamos la funcion.
# ( Que tiene muchos maximos ).

def funcion_fx(x):
return -(0.1+(1-x)**2-0.1*math.cos(6*math.pi*(1-x)))+2

# Creamos la lista decimal.

def lista_decimal(individuals,prob,pool):

   for i in range (len(individuals)):
       mutate_individual=individuals[i]
       if np.random.random() < prob:
            mutation = np.random.choice(pool[0])
             mutate_individual = [mutation] + mutate_individual[1:]
            for j in range(1,len(mutate_individual)):
                if np.random.random()<prob:
                   mutation = np.random.choice(pool[1])
                   mutate_individual = mutate_individual[0:j]+[mutation]+mutate_individual[j+1:]

             individuals[i] = mutate_individual

# Vamos con el programa principal.

x_axis=np.arange(0,2,0,02)
y_axis = np.array(list(map(funcion_fx,x_axis)))

# Nucleotidos.
ind_size = 15
genetic_pool = [[0,1],[0,1,2,3,4,5,6,7,8,9]]

# Poblacion.

# Creamos la lista.

poblacion = []

for i in range(100):
    individuo  = []
    individuo += [np.random.choice(genetic_pool[0])]
    individuo += list(np.random.choice(genetic_pool[1],ind_size-1))
    np.array(individuo)
np.array(poblacion)

# Vamos con la evolucion.
size_poblacion = len(poblacion)
generaciones = 300
for _ in range(generaciones):
    fitness = []
    for individuo in poblacion:
        x = lista_decimal(individuo)
        y = funcion_fx(x)
        fitness += [y]
    fitness = np.array(fitness)
    fitness = fitness / fitness.sum()
    offspring = []
    for i in range(size_poblacion//2):
        parents = np.random.choice(size_poblacion,2,p = fitness )
        cross_point = np.random.randint(ind_size)
        offspring += [poblacion[parents[0]][:cross_point]+poblacion[parents[1][cross_point:]]
        offspring += [poblacion[parents[1]][:cross_point]+poblacion[parents[0][cross_point:]]
    poblacion = offspring
    mutate(poblacion,0.005,genetic_pool)

# El mas aptooooo !!!!

np.np.where(fitness == fitness.max())
if np.size(n[0]) == 1:
   print(lista_decimal(poblacion[int(n[0])]))
else:
  print(" La solución no es unica " )

# Graficamos.

for individuo in poblacion:
   x = lista_decimal(individuo)
   y = funcion_fx(x)
   plt.plot(x,y,'x')

plt.plot(a_axis,y_axis)

# Terminamos :)))).
                   

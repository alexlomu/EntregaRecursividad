# EntregaRecursividad
Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/alexlomu/EntregaRecursividad)
https://github.com/alexlomu/EntregaRecursividad
Hemos resuelto diversos ejercicios de recursividad:
# Ejercicio 1: Búsqueda por dicotomía en una tabla ordenada
En este ejercicio nos piden crear un algoritmo en el que dada una tabla ordenada podamos comprobar si ese elemento forma parte de la tabla. El código es el siguiente:
```
def comprobar(tabla, busqueda, index):
    if busqueda == tabla[index]:
        print(busqueda, "si se ncuentra en la tabla, en la posición número: ", (index+1))
    if index > len(tabla):
        print(busqueda, "no se enceuntra en la tabla.")
    else:
        if index < (len(tabla)-1):
            index += 1
            comprobar(tabla, busqueda, index)

if __name__ == "__main__":
    tabla = [0, 9, 7, 5, 1, 4, 8]
    tabla.sort
    busqueda = int(input("Introduce el número que quieres comprobar si está en la lista: "))
    index = 0
comprobar(tabla, busqueda, index)
```
# Ejercicio 2: Palíndromos
En este ejercicio debemos crear un algoritmo que detecte al introducir un texto, número... si es un palíndromo. El código es el siguiente:
```
def comprobar(intro):
    if len(intro) < 1:
        print("El texto introducido es un palíndromo") 
    else:
        if intro[0] == intro [-1]:
            comprobar(intro[1:-1])
        else:
            print("El texto introducido no es un palíndromo")


if __name__ == "__main__":
    intro = input("Por favor, introduce lo que quieras comprobar si es un palíndromo: ")
    intro.lower()
    intro.replace(" ", "")
    a = "áéíóúÁÉÍÓÚ"
    b = "aeiouAEIOU"
    tildes = str.maketrans(a, b)
    intro = intro.translate(tildes)
    intro = list(intro)
comprobar(intro)
```
# Ejercicio 3: La bandera de Dijkstra
En esste ejercicio nos piden que dada una lista con las iniciales de los colores rojo, verde y azul, la ordenemos de tal manera que quede el rojo delante, luego el azul y por último el verde. El código es el siguiente:
```
#Creamos la función que ordenará por colores 
def ordenar_colores(bandera):
    if len(bandera) > 0:
        primer = bandera.pop(0)
        if primer == "R":
            red.append(primer)
            ordenar_colores(bandera)
        elif primer == "G":
            green.append(primer)
            ordenar_colores(bandera)
        elif primer == "B":
            blue.append(primer)
            ordenar_colores(bandera)
    else:
        #Definimos la nueva lista juntando las anteriores ordenadas y la mostramos
        nueva_bandera = red + blue + green
        print("La nueva bandera es", nueva_bandera)
if __name__ == "__main__":
    #Definimos la bandera
    bandera = ["R", "B", "B", "R", "G", "B", "B", "R", "B", "R", "R", "G", "R", "R", "B", "G", "G"]
    #Creamos las listas donde se ordenaran por colores
    red = []
    blue = []
    green = []
    #Llamamos a la función
    ordenar_colores(bandera)
```

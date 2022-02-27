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
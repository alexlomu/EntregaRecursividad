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
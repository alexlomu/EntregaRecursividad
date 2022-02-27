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



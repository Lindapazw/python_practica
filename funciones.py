#funciones 

def mostrarAltura():

    altura = int(input("cual es tu altura?"))

    if altura>= 180:
        print("Eres alto")
    else:
        print("Eres bajo")

mostrarAltura()
"""print("Hola mundo") #comentamos una linea

estudiante = {
    "edad" : 24,
    "nombre" : "Carlos",
    "cursos" : ["Python", "matematicas"]

}


def esAdulto():
     edad = int(input("¿Cual es tu edad?"))# 4 espacios
     if edad >= 18:
        print("Eres mayor de edad")
     else:
        print ("Eres menor de edad")


esAdulto()"""

def precioFruta():
    
    manzana = int(input("¿Cuanto cuesta la manzana? "))
    pera = int(input("¿Cuanto cuesta la pera? "))
    sumaFrutas = manzana + pera
    if sumaFrutas > 5000:
        print(f"{sumaFrutas}es mayor que 5000, no comprar")
    else : 
        print(f"{sumaFrutas}es menor que 5000, comprar")

precioFruta()






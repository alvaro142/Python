#DICCIONARIOS

#Los diccionarios en Python son una estructura que almacenan dos datos, 
# #la clave y el valor. Un ejemplo cotidiano es un diccionario físico donde buscamos el 
# #significado de una palabra y encontramos la palabra (clave) y su definición (valor). Veamos cómo se utilizan en código.

numbers = {1:"uno", 2:"dos", 3:"tres"}

print(numbers)


#extraer una parte de la información, hacer referencia a la llave
print(numbers[2])

information = {"Nombre": "Alvaro",
               "Apellido": "Mejia",
               "Altura": 1.70,
               "Edad": 38}
print(information)

del information["Edad"]
print(information)

#mostrar las claves
claves = information.keys()
print(claves)
#print(type(claves))

#Mostrar los valores 
values = information.values()
print(values)

#mostrar los pares de valor-muestra separado en tuplas las claves y los valores
pairs = information.items()
print(pairs)


contacts = {"Juanita": {"Apellido": "Muñoz",
               "Altura": 1.50,
               "Edad": 34},
            "juliana": {"Apellido": "Dominguez",
               "Altura": 1.50,
               "Edad": 58}}


print(contacts["Juanita"])
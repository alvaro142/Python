#LISTAS

to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]


print(to_do)
numbers = [1,2,3,4, "cinco"]
print(type(numbers))

mix = ["uno", 2, 3.14, True, [1,2,3]]
print(mix)
print(len(mix))
print("primer elemento", mix[0])
print("segundo elemento", mix[1])
print("ultimo elemento", mix[-1])
print(mix[0:2])
print(mix[2:])

#anexar elemento a una lista
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)

#insertar un dato en una posición en especifico en una lista
mix.insert(1,["a","b"])
print(mix)

#consultar la posición de un elemento en una lista
print(mix.index(["a","b"]))


string = "Hola Mundo"
print(string)
print("primer elemento", string[0])
print("segundo elemento", string[1])
print("ultimo elemento", string[-1])
print(string[0:2])
print(string[2:])


#consultar el elemento mayor o menor de una lista
numbers = [1,2,100.10,90.45,3,4, 5]
print("Numero Mayor es:", max(numbers))
print("Numero Menos es:", min(numbers))

#eliminar un elemento de una lista
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)

#eliminar toda la lista
del numbers
print(numbers)
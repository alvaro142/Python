#*****************GENERADORES E ITERADORES*************************

#***********ITERADORES**********************

#Iteradores: Necesitan definir explícitamente los métodos __iter__() y __next__().



#crear una lista
my_list = [1,2,3,4]

#obtener el iterador
my_iter = iter(my_list)

#usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))


#*********************ITERADORES CADENAS**************************
#creando la cadena

text = "Hola mundo"

#creando el iterador
iter_text = iter(text)

#iterar en la cadena
for char in iter_text:
    print(char)


#***********************iteradores_impares **********************
limit = 10

#crear iterador
odd_itter = iter(range(1,limit+1,2))

#usar el iterador
for num in odd_itter:
    print(num)





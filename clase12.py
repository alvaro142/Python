#BUCLES Y CONTROL DE ITERACIONES


numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print("Aqui i es igual a:",i+1)

for i in range(10):
    print(i)


#para iniciar en otro numero en este caso el numero 3
for i in range(3,10):
    print(i)

#ejemplo 1
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Guayava"]
for fruta in fruits:
    print(fruta)
    if fruta == "Naranja":
        print("Naranja encontrada")

#Ejemplo 2
fruits = ["Manzana", "Pera", "Uva", "Naranja", "Guayava"]
for fruit in fruits:
    print(fruta)
    if fruta == "Naranja":
        print("Naranja encontrada")
x = 0
while  x<5:
    if x ==3:
        break
    print(x)
    x +=1

#ejemplo 3

numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    if i ==3:
        continue
    print("Aqui i es igual a:",i+1)

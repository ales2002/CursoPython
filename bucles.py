# numero = int(input("Escriba un número para imprimir su secuencia: "))
# suma = 0
# for i in range(1,numero+1):
#     suma +=i
    
# print(suma)
    

# #calcular los numeros pares entre x recorrido y irlos sumando, y multiplicar los impares 

# numero = int(input('Escriba un número: ')) 
# suma = 0
# multiplicar = 1

# for i in range(1,numero+1):
#     print(i)
#     if i%2 ==0:
#         suma +=i
#     else:
#         multiplicar *=i
# print(suma)
# print(multiplicar)


# numeros = [1,3,4,5,5,6,5,3,4,3]
# numero = int(input('Escribe un número para verificar cuantas veces se repite en una lista: '))

# contador = 0

# for num in numeros:
#     if num == numero:
#         contador +=1
# print(contador)

# palabra ="perro"
# palabra = len(palabra)

# print(palabra)

#tabla de multiplicar 


# tabla = int(input("Escriba la tabla de multiplicar que desea saber: "))

# resultado = 0

# for i in range(1,10+1):

#     resultado = tabla*i
    
#     print(f"{tabla} * {i} = {resultado}" )

tablas = int(input("Escriba el numero de tablas que seas que se muestren los resultados de su multiplicación hasta 10: "))
result = 0
for i in range(1,tablas+1):
    print(f"Tabla de multiplicar {i}")
    for j in range(1,10+1):
        result = i*j
        print(f"{i} * {j} = {result} ")

    
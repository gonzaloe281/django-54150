# generadores
# lista = [1,2,3,4,5,6]

# for num in lista:
#     print(num)
    
# for num in range(1,7):
#     print(num)
    
    
# Lambda

# def sumav1(a,b):
#     return a+b

# print(sumav1(1,2))

# print((lambda a,b: a+b)(1,2))

# sumav2 = lambda a,b: a+b

# print(sumav2(1,2))

# Filter (es generador, termina el codigo y no vuelve a repetirse)

# lista = [1,2,3,4,5,6]


# resultado = filter( lambda valor_de_la_lista: valor_de_la_lista%2==0, lista)
# print(resultado)
# # print(list(resultado))
# # print(tuple(resultado))
# print(set(resultado))

# def es_par(valor):
#     return valor%2==0

# resultado = filter(es_par, lista)
# print(resultado)

# Map (generador tambien)

# lista = [1,2,3,4,5,6]

# resultado = map(lambda valor: valor*2, lista)
# print(resultado)
# print(list(resultado))
# print(tuple(resultado))
# print(set(resultado))

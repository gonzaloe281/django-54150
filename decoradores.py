def deco(func):
    def contenedor(a, b):
        print('primer print de deco')
        func(a, b)
        print('segundo print de deco')
    return contenedor
    
@deco
def suma(a, b):
    return a+b


print(f'el resultado entre 2 y 2 es', suma(2,2))
# Operadores Aritméticos + - * / // % **

print(2 + 2)
print(2 - 2)
print(2 * 2)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 2)
print(4 ** .5)

print('---------------------------------')

# Operadores lógicos == != < > <= >= and or not, 
#? and : True + True = True | otro caso es False
#? or: True + False = True | Basta con un verdadero para que sea verdadero
print(('z' == 'Z'))
print((1 != 1))
print(('z' == 'Z') and (1 != 1))
print(('z' == 'Z') or (1 != 1))
print(not(1 == 1) )

a = []

if not a:
    print('funcion llenar')

print('---------------------------------')
#* El valor numérico cero (0).
#* La cadena de caracteres vacía ('').
#* Las secuencias vacías (listas, tuplas, conjuntos, diccionarios vacíos).
#* El valor None.
#* Cualquier objeto personalizado que implemente el método __bool__() o __len__() y devuelva False o tenga una longitud de cero.



def verificar_valor(valor):
    if valor:
        print(f"{valor} es truthy")
    else:
        print(f"{valor} es falsy")

verificar_valor(0)        #! 0 es falsy
verificar_valor(1)        #! 1 es truthy
verificar_valor("")       #!  es falsy
verificar_valor("hola")   #! hola es truthy
verificar_valor([])       #! [] es falsy
verificar_valor([1, 2])   #! [1, 2] es truthy
verificar_valor(None)     #! None es falsy 

numero = 3

if numero % 2:
    print(numero % 2)
    print('impar')
else:
    print(numero % 2)
    print('par')

#tupla
tupla = (1,2.2, True, 'casa')

#Listas, metodo list,
        #0    1      2    3
lista = [1, 'casa', 2.3, True]
       #-4    -3    -2    -1
       
print(id(lista))
print(lista)
# lista[1] = 'Gato'
print(lista)
lista[-1] = False
print(lista)
elemento_idex_1 = lista[1]
print(elemento_idex_1)

#Desempaquetado
i1, i2, i3, i4 = lista
print(i1)
print(i2)
print(i3)
print(i4)

print('----------------------------')
tupla_mutable = list(tupla)
print(tupla)
print(tupla_mutable)
tupla_mutable[0]= '00000000000000000000'
print(tupla)
print(tupla_mutable)
tupla = tuple(tupla_mutable)
print(tupla)

print('----------------------------')
print(lista)
lista.append('Zanahoria')
print(lista)
lista.remove(2.3)
print(lista)
print('----------------------------')
print(lista)
lista2 = lista
print(lista2)
lista2.append('Ratón')
print(lista2)
print(lista)

print(id(lista))
print(id(lista2))
print('----------------------------')

lista3 = lista.copy()
lista3.append('Dirección')
print(lista3)
print(id(lista3))
print(lista2)
print(lista)




# #List Slice
print('----------------------------')
print(lista[::-1])
print(lista[::-1][0])
print(lista[::-1][-1])

estudiantes = ['juanita', 'pepito', 'maria', 'pedrito']
estudiantes_simpaticos = estudiantes[:]
print(estudiantes_simpaticos)
estudiantes[1] = 'Johanna'
print(estudiantes)
print(estudiantes_simpaticos)

#List Comprehension
print('----------------------------')

numeros = []
for i in range(-10, 1): #range siempre de menor a mayor
    numeros.append(i)
print(numeros)

#           Agre. ciclo 
numeros2 = [ i for i in range(1,11)]
print(numeros2)

numerosPar = [ i for i in range(1,11) if i % 2 == 0]
numerosImPar = [ i if i % 2 == 1 else '0' for i in range(1,11) ]
print(numerosPar)
print(numerosImPar)
#concatenar listas
[1,2,3] + [4,5,6]

# metodos de listas

#* append(): Agrega un elemento al final de la lista.
a = [1, 2.6, 'manzana', True]
a.append(100)
#! [1, 2.6, 'manzana', True, 100]

#* extend(): Extiende la lista agregando los elementos de otra lista al final.
a = [1, 2.6, 'manzana', True]
b = ['a', 'b', 'c']
a.extend(b) # o a.extend(['a', 'b', 'c'])
#! a = [1, 2.6, 'manzana', True, 'a', 'b', 'c']


#* insert(): Inserta un elemento en una posición específica de la lista.
lista = [1, 2, 3, 4, 5]
lista.insert(2, 10)
[1, 2, 10, 3, 4, 5]

#* remove(): Elimina el primer elemento de la lista que coincide con el valor dado.
lista = [1, 2, 3, 2, 4, 5]
lista.remove(2)
#! Salida: [1, 3, 2, 4, 5]

#* pop(): Elimina y devuelve el elemento en la posición dada de la lista.

lista = [1, 2, 3, 4, 5]
elemento_eliminado = lista.pop(2) #pop() vacio elemina el ultimo elemento
#!Salida: lista= [1, 2, 4, 5]
#! elemento_eliminado = lista.pop(2) | Salida: 3


#* index(): Devuelve el índice del primer elemento con el valor dado.

lista = [1, 2, 3, 4, 5]
indice = lista.index(3)
#! 2

#* count(): Devuelve el número de veces que el valor dado aparece en la lista.

lista = [1, 2, 3, 2, 4, 2, 5]
conteo = lista.count(2)
#! 3


#* sort(): Ordena los elementos de la lista en su lugar.

lista = [3, 1, 4, 1, 5, 9, 2, 6]
lista.sort()

#! lista = [1, 1, 2, 3, 4, 5, 6, 9]


#* reverse(): Invierte el orden de los elementos de la lista en su lugar.

lista = [1, 2, 4, 5, 3]
lista.reverse()
#! lista = [3, 5, 4, 2, 1]


#* copy(): Devuelve una copia superficial de la lista.
lista = [1, 2, 3, 4, 5]
copia = lista.copy()

#! copia = [1, 2, 3, 4, 5]

#* clear(): Elimina todos los elementos de la lista.
lista = [1, 2, 3, 4, 5]
lista.clear()
#! lista = []


#* len(): Devuelve la longitud de la lista.
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
#! longitud = 5


#* any(): Devuelve True si algún elemento de la lista es verdadero.

lista = [False, False, True, False]
resultado = any(lista)

#! resultado = True


#* all(): Devuelve True si todos los elementos de la lista son verdaderos.

lista = [True, True, False, True]
resultado = all(lista)

#! resultado = False


#* max(): Devuelve el elemento máximo de la lista.

lista = [3, 7, 2, 9, 5]
maximo = max(lista)

#! maximo = 9

#* min(): Devuelve el elemento mínimo de la lista.

lista = [3, 7, 2, 9, 5]
minimo = min(lista)

#! minimo = 2


#* sum(): Devuelve la suma de todos los elementos de la lista.
lista = [3, 7, 2, 9, 5]
suma = sum(lista)

#! suma = 26


#* ' '.join(iterable): Concatena los elementos de un iterable utilizando el string como separador.

palabras = ["Hola", "mundo", "Python"]
cadena_concatenada = ' '.join(palabras)

#! cadena_concatenada = Hola mundo Python

print('###########')

lista = [1,2,3,4,5]        #3
elemento = lista.pop(lista.index(4))
print(lista)
print(elemento)

num = ['ANA', 'PEDRO', 'SOL']
num = ' '.join(num).lower()
print(num)

n = [1,2,3]
l = ['a','b','c']

for n,l in zip(n,l):
    print(f'{n} - {l}')


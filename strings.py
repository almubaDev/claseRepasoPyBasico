# Concatenacion de strings, string + variable, template String f y .format

texto = 'Hola'
print(texto)
print(texto[0])
print(texto[-1])
print(texto[::2])
#Slice
c = texto[::2]
print(c)

text1 ='Chao'
text2 = 'Universo'
print('Hola' + 'Mundo') #Concatena cadena 'HolaMudo'
print('Hola' * 3) #Multiplica cadena 'HolaHolaHola'
print(text1 + text2)

#template String f y .format
text3 = ' Soy {} {}'.format(text1, text2)
text4 = f'soy {text1} {text2}'
print(text3)
print(text4)


num = 1

print('numero', 1)







#Metodos de String

#* capitalize(): Devuelve una copia del string con el primer carácter convertido a mayúscula y el resto a minúscula.
cadena = "hola mundo"
cadena_capitalizada = cadena.capitalize()
#! cadena_capitalizada = Hola mundo

#* lower(): Devuelve una copia del string con todos los caracteres convertidos a minúsculas.
#* upper(): Devuelve una copia del string con todos los caracteres convertidos a mayúsculas.
#* title(): Devuelve una versión "titulada" del string, donde cada palabra comienza con mayúscula y el resto está en minúscula.
#! 'Hola Mundo Todas Las Pal;


#* swapcase(): Devuelve una copia del string con las letras en minúscula convertidas a mayúsculas y viceversa.

cadena = "Python Es Un Lenguaje De Programación"
cadena_swapcase = cadena.swapcase()

#! cadena_swapcase = pYTHON eS uN lENGUAJE dE pROGRAMACIÓN

#* casefold(): Devuelve una versión en minúsculas del string, adecuada para comparaciones sin distinción entre mayúsculas y minúsculas.

cadena = "HOLA Mundo"
cadena_min = cadena.casefold()

#! cadena_min = hola mundo

#* count(substring, start, end): Devuelve el número de veces que aparece una subcadena en el string, opcionalmente restringido por los índices de inicio y fin.

cadena = "python es un lenguaje de programación, y Python es divertido!"
conteo = cadena.count("python")

#! conteo = 2

#* endswith(suffix, start, end): Devuelve True si el string termina con el sufijo dado, opcionalmente restringido por los índices de inicio y fin.

cadena = "Python es genial"
resultado = cadena.endswith("genial")

#! resultado =  True

#* startswith(prefix, start, end): Devuelve True si el string comienza con el prefijo dado, opcionalmente restringido por los índices de inicio y fin.

cadena = "Python es genial"
resultado = cadena.startswith("Python")

#! resultado = True

#* find(substring, start, end): Devuelve el índice de la primera aparición de una subcadena en el string, o -1 si no se encuentra, opcionalmente restringido por los índices de inicio y fin.

cadena = "Python es un lenguaje de programación, y Python es divertido!"
indice = cadena.find("Python")

#! indice = 0


#* index(substring, start, end): Similar a find(), pero genera una excepción ValueError si no se encuentra la subcadena.

cadena = "Python es un lenguaje de programación, y Python es divertido!"
indice = cadena.index("Python")

#! indice = 0
#! ValueError si no lo encuentra


#* isalnum(): Devuelve True si todos los caracteres del string son alfanuméricos (letras o números).
#* isalpha(): Devuelve True si todos los caracteres del string son letras.
#* isdigit(): Devuelve True si todos los caracteres del string son dígitos.
#* islower(): Devuelve True si todos los caracteres del string están en minúsculas.
#* isupper(): Devuelve True si todos los caracteres del string están en mayúsculas.
#* isspace(): Devuelve True si todos los caracteres del string son espacios en blanco.



#* strip(chars): Elimina los caracteres iniciales y finales especificados (o espacios en blanco si no se proporciona ningún argumento).
cadena = "  ¡Hola Mundo!  "
cadena_limpia = cadena.strip()

#! cadena_limpia = ¡Hola Mundo!
#* lstrip(chars): Elimina los caracteres iniciales especificados (o espacios en blanco si no se proporciona ningún argumento).
#* rstrip(chars): Elimina los caracteres finales especificados (o espacios en blanco si no se proporciona ningún argumento).


#* replace(old, new, count): Devuelve una copia del string con todas las ocurrencias de la subcadena "old" reemplazadas por la subcadena "new", opcionalmente limitada por el número máximo de reemplazos "count".
cadena = "python es un lenguaje de programación, y Python es divertido!"
cadena_reemplazada = cadena.replace("Python", "Java")

#! cadena_reemplazada = python es un lenguaje de programación, y Java es divertido!


#* zfill(width): Rellena el string con ceros a la izquierda hasta alcanzar la longitud especificada.

cadena = "42"
cadena_zfilled = cadena.zfill(5)

#! cadena_zfilled = '00042'


#* split(separator, maxsplit): Divide el string en una lista de subcadenas usando el separador dado, opcionalmente limitado por el número máximo de divisiones.
cadena = "Python es un lenguaje de programación"

lista_palabras = cadena.split()

#!lista_palabras = ['Python', 'es', 'un', 'lenguaje', 'de', 'programación']


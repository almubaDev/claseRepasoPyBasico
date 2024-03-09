#Diccionarios, creacion, llave, valor, reasignacion, Comprehension Dict

#* clear(): Elimina todos los elementos del diccionario.

diccionario = {'a': 1, 'b': 2, 'c': 3}
diccionario.clear()

#! diccionario = {}

#* copy(): Devuelve una copia superficial del diccionario.

diccionario_original = {'a': 1, 'b': 2, 'c': 3}
diccionario_copia = diccionario_original.copy()

diccionario_copia['d'] = 4

#! diccionario_original = {'a': 1, 'b': 2, 'c': 3}
#! diccionario_copia = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#* fromkeys(keys, value): Crea un nuevo diccionario con las claves dadas y el valor dado para cada clave.

nuevo_diccionario = dict.fromkeys(['a', 'b', 'c'], 0)
#! nuevo_diccionario = {'a': 0, 'b': 0, 'c': 0}

#* get(key, default): Devuelve el valor asociado con la clave dada; si la clave no existe, devuelve el valor predeterminado (None si no se proporciona).

diccionario = {'a': 1, 'b': 2, 'c': 3}
valor_a = diccionario.get('a')
valor_d = diccionario.get('d', 0)

#! valor_a = 1
#! valor_d = 0


#* items(): Devuelve una vista de pares (tuplas) clave-valor en el diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
vista_items = diccionario.items()

#! vista_items = dict_items([('a', 1), ('b', 2), ('c', 3)])

#* keys(): Devuelve una vista de las claves en el diccionario.

diccionario = {'a': 1, 'b': 2, 'c': 3}
vista_claves = diccionario.keys()

#! vista_claves = dict_keys(['a', 'b', 'c'])

#* values(): Devuelve una vista de los valores en el diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
vista_valores = diccionario.values()

#! vista_valores = dict_values([1, 2, 3])

#* pop(key, default): Elimina y devuelve el valor asociado con la clave dada; si la clave no existe, devuelve el valor predeterminado (o genera una excepción si no se proporciona).

diccionario = {'a': 1, 'b': 2, 'c': 3}
valor_b = diccionario.pop('b')
valor_d = diccionario.pop('d', 0)

#! valor_b = Salida: 2
#! valor_d = 0
#! diccionario = {'a': 1, 'c':3}



#* update(other): Actualiza el diccionario con los pares clave-valor del otro diccionario u otro iterable de pares clave-valor.
diccionario = {'a': 1, 'b': 2}
otro_diccionario = {'b': 3, 'c': 4}

diccionario.update(otro_diccionario)

#! diccionario ={'a': 1, 'b': 3, 'c': 4}


#* del: Elimina un elemento del diccionario por su clave.
diccionario = {'a': 1, 'b': 2, 'c': 3}

del diccionario['b']

#! diccionario = {'a': 1, 'c': 3}

#* len(): Devuelve el número de elementos en el diccionario.
#* in: Verifica si una clave está presente en el diccionario.
#* clear(): Elimina todos los elementos del diccionario.


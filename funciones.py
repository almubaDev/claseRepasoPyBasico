#Declaraciones  de funcion, retorno



#funciones lambda parametros: expresion



#Tipos de argumento
# Posicionales
def saludar(saludo, nombre, apellido):
    return f'{saludo}, {nombre} {apellido}'
saludar('Hola', 'Alan', 'Muñoz')
#! "Hola Alan Munoz"
saludar('Alan', 'Hola' ,'Muñoz')
#! "Alan Hola Munoz"


# Por defecto y Por nombre (keyword arguments)
def saludar(saludo='Buenos días', nombre='Sol', apellido='Martinez'):
    return f'{saludo}, {nombre} {apellido}'

saludar('Hola', 'Alan', 'Muñoz')
#! "Hola Alan Munoz"
saludar('Alan', 'Hola' ,'Muñoz')
#! "Alan Hola Munoz"
saludar()
#! "Buenos días Sol Martines"
saludar('Alan', 'Munoz')
#! "Alan Munoz Martinez"
saludar(nombre='Alan', apellido='Munoz')
#! "Buenos días Alan Munoz"


# De longitud variable (*args)
def nombres(*args):
    print(type(args))
    print(args)
    for nombre in args:
        print(nombre)

nombres('Alan', 'Pascal', 'Julio')
#! <class 'tuple'>
#! ('Alan', 'Pascal', 'Julio')
#! 'Alan'
#!  'Pascal'
#!  'Julio'

# De longitud variable con nombres (**kwargs)
def format_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, values in kwargs.items():
        print(key,' - ', values)

format_data(nombre='Alan', edad=35, correo='alan@example.com')
#! <class 'dict'>
#! {'nombre': 'Alan', 'edad': 35, 'correo': 'alan@example.com'}
#! nombre  -  Alan
#! edad  -  35
#! correo  -  alan@example.com
 
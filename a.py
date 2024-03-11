list_dict = []

for i in range(1,4):
    nombre = input('nombre: ')
    edad = input('edad: ')
    
    list_dict.append(
        {
        'nombre': nombre,
        'edad' : edad
        }
    )

print(list_dict)
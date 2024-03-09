# if, elif, else
frutas = ['manzana', 'kiwi', 'pera']
verduras = ['apio', 'acelga', 'brocoli']

ingrediete_1 = 'manzana'
ingrediete_2 = 'pera'

if ingrediete_1 in frutas and ingrediete_2 in frutas:
    print('Es un tuti-fruti')
    
elif ingrediete_1 in verduras and ingrediete_2 in verduras:
    print('Es una ensalada')
else:
    print('Ensalada de frutas')



if ingrediete_1 in frutas and ingrediete_2 in frutas:
    print('Es un tuti-fruti')

if ingrediete_1 in frutas and ingrediete_2 in frutas:
    print('Al usuario solo le gusta la fruta')   



term = 5
match term:
    case 1:
        print("Acción 1")
    case 2:
        print("Acción 2")
    case 3:
        print("Acción 3")
    case _:
        print("Acción por defecto")
#? Caso cohete

def enfriamiento(temperatura):
    temperatura = int(temperatura)
    print(temperatura)
    if temperatura == 14.5:
        print("Enfriminento encendido")
    elif temperatura > 14.5:
        print("El cohete a explotado")
        exit()


temp = 0.0      
while True:
    temp += 0.1
    enfriamiento(temp)
    
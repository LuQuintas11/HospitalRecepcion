import random

sint=[];
lista=[];
paciente_nombre=[];





def validar_data(paciente_nombre):
    """
    Funcion para validar nombre del paciente
    """
    is_valid_name = paciente_nombre.replace(" ", "").isalpha()
    
    

    if not is_valid_name:

        print("Ingresa un nombre valido")

    return is_valid_name



paciente_nombre=(input("Cual es tu nombre?:"));
list(paciente_nombre)
print("".join(paciente_nombre))



while not validar_data(paciente_nombre):

   paciente_nombre=(input("Cual es tu nombre?:"));
   

print(f"Hola {paciente_nombre}. Estamos preparado para ingresarte!")
sint.append(paciente_nombre)


while True:
    
        try:
            sint.append(int(input("Tenes algunos de los siguientes sintomas: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria")))
        except ValueError:
            print("Ingresa una opcion correcta: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria")
            continue;
            
            
        print(sint)
        salir=input("Desea ingresar otro sintoma?: Si/No")
        if salir == 'S': 
            continue;
        else:
            if len(sint)>=3:
                numero_1=random.randint(0,1000)
                nombre.append(numero_1)
                print(nombre)
            elif len(sint)==2:
                numero_2=print(random.randint(1000,3000))
                nombre.append(numero_2)
                print(nombre)
            else:
                numero=print(random.randint(3000,5000))
    
            break;

    





    

        





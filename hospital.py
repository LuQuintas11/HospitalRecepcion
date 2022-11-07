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

def main_adulto(paciente_nombre):

    while True:
    
        try:
            sint.append(int(input("Tenes algunos de los siguientes sintomas?: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria 4. Dolor torácico intenso 5. Hemorragia severa 6.Fracturas  ")))
        except ValueError:
            print("Ingresa una opcion correcta: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria 4. Dolor torácico intenso 5. Hemorragia severa 6.Fracturas  ")
            continue;
       
        salir=input("Desea ingresar otro sintoma?: Si/No")
        if salir == 'Si': 
            continue;
        else:
            if len(sint)>=3:
                numero_1=random.randint(0,1000)
                [paciente_nombre].append(numero_1)
                print([paciente_nombre])
                print(numero_1)
            elif len(sint)==2:
                numero_2=print(random.randint(1000,3000))
                [paciente_nombre].append(numero_2)
                print([paciente_nombre])
            else:
                numero=print(random.randint(3000,5000))
    
            break;

def main_pediatrico(paciente_nombre):

    while True:
    
        try:
            sint.append(int(input("Tenes algunos de los siguientes sintomas: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria 4. Dolor torácico intenso 5. Hemorragia severa 6.Fracturas 7. Convulsiones ")))
        except ValueError:
            print("Ingresa una opcion correcta: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria 4. Hemorragia severa 5.Fracturas 6. Convulsiones ")
            continue;
       
        salir=input("Desea ingresar otro sintoma?: Si/No")
        if salir == 'Si': 
            continue;
        else:
            if len(sint)==3 and '4' in sint:
                numero_1=print(random.randint(0,500))
                #paciente_nombre.append(numero_1)
                print(paciente_nombre)
                print(numero_1)

            elif len(sint)>=3:
                numero_2=random.randint(500,1000)
                #paciente_nombre.append(numero_2)
                print(paciente_nombre)
                print(numero_2)
            elif len(sint)==2:
                numero_3=print(random.randint(1000,3000))
                #nombre.append(numero_3)
                print(paciente_nombre)
                print(numero_3)
            else:
                numero=print(random.randint(3000,5000))
    
            break;



def main_ingreso():

    """ funcion que ingresa el nombre y sintomas
        del paciente """
    
    print("Bienvenido a Clinica del Sol")
    paciente_nombre=(input("Cual es tu nombre y apellido?:"));

    try:
        paciente_edad=(int(input("Cual es tu edad?:")));
    except ValueError:
        print("Ingresa un valor correcto");
        
        


    while not validar_data(paciente_nombre):
        paciente_nombre=(input("Cual es tu nombre?:"));
   

    print(f"Hola {paciente_nombre}. Estamos preparado para ingresarte!")   

    if paciente_edad<18:
        main_pediatrico(paciente_nombre);
    else:
        main_adulto(paciente_nombre);


main_ingreso();
    
    
    






    

        





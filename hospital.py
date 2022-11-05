import random

sint=[];
lista=[];
nombre=[];

nombre.append(input("Cual es tu nombre:"));
nombre.append(input("Cual es tu apellido:"))
print(nombre)

while True:
    
    
        sint.append(input("Tenes algunos de los siguientes sintomas: 1.Fiebre  2.Vomitos 3.Dificultad Respiratoria"))
        
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

    





    

        





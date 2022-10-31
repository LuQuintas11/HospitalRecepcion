import random
sint=[];
numero=""
input("Cual es tu nombre:");

while True:
    sint.append(input("Tenes algunos de los siguientes sintomas: 1.Fiebre  2.Vomitos  3.Dificultad Respiratoria 4. No tengo ninguno de estos sintomas"))
    print('Ademas posees alguno otro sintomas')
    if '4' in sint:
        break;
print(sint)
if len(sint)>=3:
    numero=print(random.randint(0,1000))
    """en google sheet al medico le va a aparecer como paciente super prioritario"""
elif len(sint)==2:
    numero=print(random.randint(1000,3000))
else:
    numero=print(random.randint(3000,5000))



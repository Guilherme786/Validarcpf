import sys

def NumerarCPF():
    for a in cpf:
        a = int(a)
        cpf_numero.append(a)

def quantidade():
        if len(cpf) < 11 or len(cpf) > 11:
            return False
        else:
            return True

def primeiro_digito():
    if len(cpf_numero) < 11 or len(cpf_numero) > 11:
        return False
    else:
        acumulador = 0
        resultado = 0
        controlador = 10
        for numeros in cpf_numero[0:9]:
            resultado = numeros *controlador
            acumulador += resultado
            controlador = controlador - 1
        acumulador = acumulador * 10 % 11
        if acumulador == 10:
            acumulador = 0 
        if acumulador == cpf_numero[9]:
            return True
        else:
            return False
               
def segundo_digito():
    if  len(cpf_numero) < 11 or len(cpf_numero) > 11:
        return False
    else:
        acumulador2 = 0
        resultado2 = 0
        controlador2 = 11
        for numeros2 in cpf_numero[0:10]:
            resultado2 = numeros2 * controlador2
            acumulador2 += resultado2
            controlador2 = controlador2 - 1
        acumulador2 = acumulador2 * 10 % 11
        if acumulador2 == 10:
            acumulador2 = 0 
        if acumulador2 == cpf_numero[10]:
            return True
        else:
            return False

cpf_numero = []
cpf = str(input("Digite seu CPF:")).replace('.','').replace('-','')

NumerarCPF()

quantidade()

primeiro_digito()

segundo_digito()

if quantidade() == True and primeiro_digito() == True and segundo_digito() == True:
    print("O Cpf é valido")

else:
    print("O Cpf é invalido")

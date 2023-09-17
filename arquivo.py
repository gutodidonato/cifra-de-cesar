import random as r

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numero = r.randint(0,25)



def criptografar(frase):
    frase_nova = ""
    for j in range(len(frase)):
        if frase[j] in alfabeto:
            indice = alfabeto.index(frase[j])
            indice_novo = ((indice + numero) % 26)
            frase_nova += alfabeto[indice_novo]
        else:
            '''caso numero ou espaço'''
            frase_nova += frase[j]
    print(frase_nova)
    print(numero)
    print("\n")
    return numero
            
def decriptografar(numero, frase): 
    frase_dec = ""          
    for i in range(len(frase)):
        if frase[i] in alfabeto:
            indice = alfabeto.index(frase[i])
            indice_novo = (indice - numero) % 26
            frase_dec += alfabeto[indice_novo]
        else:
            frase_dec += frase[i]
    print(frase_dec + "\n")

resposta = ""
while (resposta != "sair"):
    vontade = input("Deseja criptografar ou decriptografar? ")
    if vontade == "criptografar":
        criptografar(input("diga sua frase: "))
    elif vontade == "decriptografar":
        decriptografar(int(input("Diga o numero de codificação ")), input("Diga a frase "))
    else:
        resposta = "sair"
                       
nome = "Thaissa"

print (nome)

def soma (x, y):
    resultado =  x + y
    return resultado

def simples (cor):
    if cor == 'azul':
        return 'escolheu certo'
def medio(cor):
    if cor == 'azul':
        return 'escolheu certo'
    else:
        return 'tente outra cor'
        
def completo(cor):
    if cor == 'azul':
        return 'boa'
    elif cor == 'roxo':
        return 'okay'
    elif cor == 'preto':
        return 'legal'
    elif cor == 'laranja':
        return 'ruim'
    elif cor == 'amarelo':
        return 'maneiro'
        
numeros = [1, 2, 3, 4, 5]
print(numeros[0])
print(numeros[-1])
numeros[0] = 10
print(numeros)
contador = 0

while contador < 10:
    print(contador)
    contador += 1

for i in range(10):
    print(i)

for item in [1,45,78,'a',[3,5]]:
    print(item)

for letra in 'minha string':
    print(letra)


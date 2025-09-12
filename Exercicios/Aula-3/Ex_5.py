dados = {}

n = int(input("Quantas pessoas serão cadastradas?"))


for g in range(n):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: M ou F ')
    dados[nome] = [idade, sexo]

media = 0

menos_20 = 0

for idade, sexo in dados.values():
    media += idade
    if sexo == 'F' and idade < 20:
        menos_20 += 1

media /= len(dados)

print("A média da idade de todos é {}".format(media))
print("Existem {} mulheres com menos de 20 anos".format(menos_20))
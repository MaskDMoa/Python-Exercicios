nome = input('Nome do Aluno: ')

media = int(input('Media do Aluno: '))

dados = {'Aluno':nome, 'Media':media}

if dados['Media'] >= 50:
    print('Aprovado')
    dados['Situação'] = 'Aprovado' 
else:
    print('Reprovado')
    dados['Situação'] = 'Reprovado'

print(dados)
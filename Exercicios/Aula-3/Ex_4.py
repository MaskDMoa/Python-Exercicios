dados = {} 

for g in range(3): 
    nome = input("Nome: ") 
    peso = float(input("Peso: ")) 
    dados[nome] = peso 
    
mais_pesado = max(dados, key=dados.get) 
mais_leve = min(dados, key=dados.get) 

print('O mais pesado é {} com {} kg'.format(mais_pesado, max(dados.values()))) 
print('O mais leve é {} com {} kg'.format(mais_leve, min(dados.values())))
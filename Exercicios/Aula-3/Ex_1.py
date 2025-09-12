lista = ['Flamengo', 'Cruzeiro', 'Palmeiras', 'Bahia', 'Mirassol']

print("3 primeiros colocados:", lista[:3])

print("2 últimos colocados:", lista[-2:])

print("Times em ordem alfabética:", sorted(lista))

if 'Barcelona' in lista:
    posicao = lista.index('Barcelona') + 1 
    print(f"Barcelona está na {posicao}ª posição.")
else:
    print("Barcelona não está na lista.")

loja1 = {'Samsung Galaxy S23', 'Motorola Edge 40', 'Xiaomi Redmi Note 13', 'Asus ROG Phone 7', 'Realme GT Neo 5', 'Samsung Galaxy S23', 'Motorola Edge 40'}
loja2 = {'iPhone 15 Pro Max', 'Google Pixel 8 Pro', 'OnePlus 11', 'Huawei P60 Pro', 'Oppo Find X6 Pro', 'Samsung Galaxy S23', 'Motorola Edge 40'}

print('Na loja1 você terá a opção de comprar {}'.format(loja1))
print('Na loja2 você terá a opção de comprar {}'.format(loja2))

todos = loja1 | loja2

print('Modelos disponíveis no total: {}'.format(todos))

mesmos = loja1 & loja2

print('Modelos que existem nas duas lojas: {}'.format(mesmos))
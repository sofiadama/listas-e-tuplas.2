lista = [9, 3, 2, 4, 3]

par = []
for x in lista:
    if x % 2 == 0:
        par.append(x)
        
print(f'{lista.count(9)} ocorrência')
print(f'{lista.index(3)+1}º posição')
print(f'Pares: {par}')

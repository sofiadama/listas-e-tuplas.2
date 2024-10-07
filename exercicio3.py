numeros = []

for i in range(10):
    inteiros = int(input(f'{i+1}º número: '))
    numeros.append(inteiros)

contagem = 0
for x in set(numeros):
    if numeros.count(x) > 1:
        contagem += 1
        
print()
print(f'Números repetidos: {contagem}')

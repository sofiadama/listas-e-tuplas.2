import random

numeros = []
for i in range(5):
    aleatorios = random.randint(0,100)
    numeros.append(aleatorios)

print(*numeros)
print()
print(f'Maior número: {max(numeros)}')
print(f'Menor número: {min(numeros)}')
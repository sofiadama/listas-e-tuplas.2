import math
testes = int(input('Testes: '))

for i in range(testes):
    A,R = list(map(int,input().split()))
    tentativas = list(map(int,input('Número: ').split()))[:A]
    
    R = float(R)
    for n in tentativas:
        if n == R or n == math.floor(R):
            posicao = tentativas.index(n)
            print(f'{posicao+1}º aluno correto!')

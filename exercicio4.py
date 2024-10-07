import math
testes = int(input('Testes: '))

for i in range(testes):
    A,R = list(map(int,input().split()))
    tentativas = list(map(int,input('Número: ').split()))[:A]
    
    R2 = math.floor(R)
    for n in tentativas:
        if n == R or n == R2:
            posicao = tentativas.index(n)
            print(f'{posicao+1}º aluno correto!')

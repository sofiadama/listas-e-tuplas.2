testes = int(input('Testes: '))

for i in range(testes):
    A,R = list(map(int,input('Alunos e resposta: ').split()))
    tentativas = list(map(int,input('Tentativas: ').split()))[:A]
   
    found = False
    if R in tentativas:
        posicao = tentativas.index(R)
        print(f'{posicao+1}º aluno correto!')
        found = True
        
    else:
        proximo = [(abs(R - n), i) for i, n in enumerate(tentativas)]
        proximo.sort()
        posicao = proximo[0][1]
        print(f'{posicao+1}º aluno correto!')

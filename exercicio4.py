testes = int(input('Testes: '))

i = 0
while i < testes:
    QT,S = input().split()
    QT = int(QT)
    S = int(S)
    
    tentativas = (map(int,input('Número: ')[:QT]))
    for numeros in tentativas:
        if numeros == S:
            print(f'{QT}º aluno correto!')


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media: float = (n1 + n2) / 2

print('A média do aluno é {}'.format(media))

if media >= 7:
    print('Aluno Aprovado')
else:
    print('Aluno Reprovado')



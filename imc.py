peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / altura ** 2

print('O seu IMC é :{}'.format(imc))

if imc < 18.5:
    print('Você está com magreza')

elif 18.5 <= imc < 25:
    print('Seu peso está Normal')

elif 25 <= imc < 30:
    print('Você está com Sobrepeso')

elif 30 <= imc < 35:
    print('Você está com Obesidade Grau I')

elif 35 <= imc < 40:
    print('Você está com Obesidade Grau II Severa!!!')

elif imc >= 40:
    print('Você está com Obesidade Grau III Morbida')

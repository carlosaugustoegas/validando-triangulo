import math



print('='* 40)
print('{:^40}'.format('DESAFIO DOS TRIÂNGULOS'))
print('='* 40)
ladoA = int(input('Digite o 1o lado: '))
ladoB = int(input('Digite o 2o lado: '))
ladoC = int(input('Digite o 3o lado: '))

triangulo = abs(ladoB - ladoC) < ladoA and ladoA < ladoB + ladoC and abs(ladoA - ladoC) < ladoB and ladoB < ladoA + ladoC and abs(ladoA - ladoB) < ladoC and ladoC < ladoA + ladoB

equilatero = ladoA == ladoB and ladoA == ladoC and ladoB == ladoC

escaleno = ladoA != ladoB and ladoA != ladoC and ladoB != ladoC

isosceles = (ladoA == ladoB and ladoA != ladoC) or (ladoB == ladoC and ladoB != ladoA)

print('='* 40)
print('{:^40}'.format('RESULTADO:'))
print('='* 40)
print('Valores digitados: {}, {} e {}.'.format(ladoA, ladoB, ladoC))
print('Triângulo: {}'.format(triangulo))
if not triangulo:
    print('Não é possível existir um triângulo')

if triangulo and equilatero:
    print('É um triângulo equilatero!')
    
if triangulo and isosceles:
    print('É um triângulo isosceles')

elif triangulo and escaleno:
    print('É um triângulo escaleno!')




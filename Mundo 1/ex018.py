from math import radians, sin, cos, tan

print('ANGULOS')
print('-'*7)

a = float(input('Digite o angulo:'))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print('Para o Angulo: {}, temos o Seno: {:.2f}, Cosseno: {:.2f} e Tangente: {:.2f}'.format(a, sen, cos, tan))



print('Analisando Triangulos v2.0')
print('-'*26)

s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1+s2:
    print('Os Segmentos acima PODEM FORMAR um Trisangulo', end='')
    if s1 == s2 == s3:
        print(' Equilatero')
    elif s1 != s2 != s3 != s1:
        print(' Escaleno')
    else:
        print(' Isosceles')
else:
    print('Os Segmentos acima NÃO PODEM FORMAT um Triangulo.')

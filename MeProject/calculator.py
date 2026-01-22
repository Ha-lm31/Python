# python calculator.py
# 22-01-2026
# Mon premier essay en python, la version 1 du calculatruce, 
# je veux améliorer pour etre bien au future
# Quand on tap l'opération il faut afficje le next nombre??
print('Quelle Operation vous pouvez faire :')

x = int(input('le 1 nombre '))
y = input('l\'operation ')
z = int(input('le 2 nombre '))
if(y=='+'):
    a = x+z
if(y=='-'):
    a = x-z
if(y=='*'):
    a = x*z
if(y=='/'):
    a = x/z
print('le résultat est ',a)
from re import I


print('''Уравнение ax+b=0 давайте найдём x при выбраных a и b.''')
a=input()
b=input()
a=int(a)
b=int(b)

if(a==0 and b==0):
    print('inf')

if(a==0 and b!=0):
    print('no')

if(a!=0 and b%a!=0):
    print('no')

if(a!=0 and b%a==0):
    n = int(b/a)
    print(n)
    
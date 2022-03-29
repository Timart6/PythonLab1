#16. Визначити число, яке отримано записом у зворотньому порядку цифр заданого тризначного числа.

def Invert(x):

    a = x//100
    x = x - a*100
    b = x//10
    x = x - b*10
    c = x
    x = c*100 + b*10 + a
    print(x)
print('Enter 3-digit number')
x = int(input())
Invert(x)
input()

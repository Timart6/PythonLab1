#1. Дана сторона квадрата a. Знайти його периметр P=4·a
def Perimeter(a):
    P = 4*a
    return print('Perimeter =',P)


print('Enter square side')
a = int(input())
Perimeter(a)
input()
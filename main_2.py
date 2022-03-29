# 2. Дана сторона квадрата a. Знайти його площу S=a^2

def Area(a):
    S = a**2
    return print('Square area =',S)
print('Enter a square side')
a = int(input())
Area(a)
input()
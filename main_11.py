#11. Знайти значення функції y=3x^6+6x^2+7 при даному значенні x

def Function(x):
    y=3*(x**6)+6*(x**2)+7
    return print(y)
print('Enter x')
x = int(input())
Function(x)
input()
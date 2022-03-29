#6. Поміняти місцями вміст змінних A і B і вивести нові значення A і B.
def Change(A,B):
    C = A
    A = B
    B = C
    print('Result: ')
    print('value A: ' + A)
    print('value B: ' + B)

print('Print value A: ')
A = input()
print('Print value B: ')
B = input()
Change(A,B)
input()


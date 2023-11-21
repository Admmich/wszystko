import math
# a=0.10000
# b=150
# c=5
# delta = b*b-4*a*c
# #math.sqrt(delta)
# print(delta)

#napisz program podajacy winik obliczenia zamiany ulamka binarnego na liczby dziesietne przezanianie podajemy ilosc bitow na jakich jest zapisana podana liczxba
# def binToFloat(n, ileBit=0):
#     wynik = 0
#     for i in range(2, ileBit+2):
#         if n[i] == '1' or n[i] == '0':
#             if n[i] == '1':
#                 wynik += 2 ** (-i+1)
#         else:
#             return  "ERROR"
#     return wynik
#
# print(binToFloat("0,000110011001100110011001100110011", 4))

# eps = 0.00001
#
# skladowa = 1
# i=1
# wynik = 0
# while skladowa > eps:
#     i += 2
#     skladowa += skladowa / i
#     skladowa /= i
#     print(skladowa)

def silnia(n):
    w = 1
    for i in range(1, n+1):
        w *= i
    return w
def zadanie():
    eps = 0.0001
    wynik = 1.0
    k = 3
    skladnik = 1/silnia(k)
    znak = -1
    while skladnik >= eps:
        wynik += znak * skladnik
        k += 2
        skladnik = 1 / silnia(k)
        znak = -znak
    return wynik
print(zadanie())

praca domowa
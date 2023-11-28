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

# def silnia(n):
#     w = 1
#     for i in range(1, n+1):
#         w *= i
#     return w
# def zadanie():
#     eps = 0.0001
#     wynik = 1.0
#     k = 3
#     skladnik = 1/silnia(k)
#     znak = -1
#     while skladnik >= eps:
#         wynik += znak * skladnik
#         k += 2
#         skladnik = 1 / silnia(k)
#         znak = -znak
#     return wynik
# print(zadanie())

# def los(n):
#     t=[]
#     for i in range(n):
#         t.append(randint(0,200))
#     return
# t = los(11)
# y=[]
# def quicksort(arr,l=0,r=None):
#     if r is None:
#         r=len(arr)-1
#     i=l
#     j=r
#     pivot=arr[(l+r)//2]
#     y.append(pivot)
#     while i <=j:
#         while arr[i]<pivot:
#             i+=1
#         while arr[i]>pivot:
#             j-=1
#         if i <=j:
#             arr[i],arr[j]=arr[j],arr[i]
#             i +=1
#             j -=1
#         if l < j:
#             quicksort(arr,l,j)
#         if r > i:
#             quicksort(arr,i,r)
# print(t)
# quicksort(t)
# print(t)
# print(y)


from random import choices

def los(n):
    return choices((1,2,3,4,5,6), k=n)

def rzut(pkt, rzut_kostka):
    if rzut_kostka == 6:
        return pkt
    if rzut_kostka in (5,4):
        return pkt * 2
    if rzut_kostka == 3 or rzut_kostka == 2:
        return  pkt //2
    if rzut_kostka == 1:
        return 1


def rezultat(pkt, tab):
    for i in tab:
        pkt = rzut(pkt, i)
    return pkt

tab = los(3)
print(tab)
print(rezultat(100,tab))


halo
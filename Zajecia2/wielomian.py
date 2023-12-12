# def indeks(tekst, litera):
#     indeks1 = []
#     for i, znak in enumerate(tekst):
#         if znak == litera:
#             indeksy.append(i)
#     return indeks
#
#
# print(indeks(python, t))
#
# lista = ['Adam Nowak', 'Jan Kowalski', 'Piotr Baran']
# inicjal = []
# for i in lista:
#     imie_nazw = i.split()
#     imie, nazw = imie_nazw[0], imie_nazw[1]
#     inicjal.append(imie[0] + nazw[0])
#
# print(inicjal)
# #zad 3
# def najdzzwzorz(tekst, wzorzec):
#     for i in tekst:
#         for j in wzorzec:
#             if i == j:
#                 return True
#             else:
#                 return False
# # x = 0
# # while x!=1:
# #     print(x)
# #     x += 1/10
#
#
#
# # x=0
# # i = 0.100000
# # while x<1:
# #     x = x + i
# #     print(x)
#
# #napisz program podajacy wynik obliczenia zamiany ulamka binarngo na liczbe dziesietna przy zamianie podajemy ilosc bitow na jakich jest zapisana podana liczba
# # def BinToFloat(n, ileBit=0):
# #     wynik = 0
# #     for i in range(2, ileBit+2):
# #         if n[i] == '1' or n[i] == '0':
# #             if n[i]=='1':
# #                 wynik += 2 ** (-i + 1)
# #         else:
# #             return "ERROR"
# #     return wynik
# #
# # print(0.1 - BinToFloat("0,000110011001100110011", 8 ))
# # print(0.1 - BinToFloat("0,000110011001100110011", 12 ))
# # print(0.1 - BinToFloat("0,000110011001100110011", 16 ))
# #wartosc dokladna x= 0,1 w systemie dziesietnym jest rowna 0,1 oblicz jaki bedzie blad przy zapisie liczby 0,1 z wykorzystaniem 8 bitow 12 bitow i 16 bitow
#
#
# from random import choices
#
#
# def los(n):
#     return choices((1, 2, 3, 4, 5, 6), k=n)
#
#
# def rzut(pkt, rzut_kostka):
#     if rzut_kostka == 6:
#         return pkt
#     if rzut_kostka in (5, 4):
#         return pkt * 2
#     if rzut_kostka == 3 or rzut_kostka == 2:
#         return pkt // 2
#     if rzut_kostka == 1:
#         return 1
#
#
# def rezultat(pkt, tab):
#     for i in tab:
#         pkt = rzut(pkt, i)
#     return pkt
#
#
# tab = los(3)
# print(tab)
# print(rezultat(100, tab))
#
# import math
# # a=0.10000
# # b=150
# # c=5
# # delta = b*b-4*a*c
# # #math.sqrt(delta)
# # print(delta)
#
# #napisz program podajacy winik obliczenia zamiany ulamka binarnego na liczby dziesietne przezanianie podajemy ilosc bitow na jakich jest zapisana podana liczxba
# # def binToFloat(n, ileBit=0):
# #     wynik = 0
# #     for i in range(2, ileBit+2):
# #         if n[i] == '1' or n[i] == '0':
# #             if n[i] == '1':
# #                 wynik += 2 ** (-i+1)
# #         else:
# #             return  "ERROR"
# #     return wynik
# #
# # print(binToFloat("0,000110011001100110011001100110011", 4))
#
# # eps = 0.00001
# #
# # skladowa = 1
# # i=1
# # wynik = 0
# # while skladowa > eps:
# #     i += 2
# #     skladowa += skladowa / i
# #     skladowa /= i
# #     print(skladowa)
#
# # def silnia(n):
# #     w = 1
# #     for i in range(1, n+1):
# #         w *= i
# #     return w
# # def zadanie():
# #     eps = 0.0001
# #     wynik = 1.0
# #     k = 3
# #     skladnik = 1/silnia(k)
# #     znak = -1
# #     while skladnik >= eps:
# #         wynik += znak * skladnik
# #         k += 2
# #         skladnik = 1 / silnia(k)
# #         znak = -znak
# #     return wynik
# # print(zadanie())
#
# # def los(n):
# #     t=[]
# #     for i in range(n):
# #         t.append(randint(0,200))
# #     return
# # t = los(11)
# # y=[]
# # def quicksort(arr,l=0,r=None):
# #     if r is None:
# #         r=len(arr)-1
# #     i=l
# #     j=r
# #     pivot=arr[(l+r)//2]
# #     y.append(pivot)
# #     while i <=j:
# #         while arr[i]<pivot:
# #             i+=1
# #         while arr[i]>pivot:
# #             j-=1
# #         if i <=j:
# #             arr[i],arr[j]=arr[j],arr[i]
# #             i +=1
# #             j -=1
# #         if l < j:
# #             quicksort(arr,l,j)
# #         if r > i:
# #             quicksort(arr,i,r)
# # print(t)
# # quicksort(t)
# # print(t)
# # print(y)
#
#
# # import xxxxxxxxxx from lol.py
#
#
#
#
#
# # lista=[[],[]]
# # wyr = '1 * 2 * (3 + 4)'
# #
# # for i in wyr:
# #     if ord(i) <= 57 and ord(i) >= 48 :
# #         lista[0].append(i)
# #     else:
# #         lista[1].append(i)
# #
# # print(lista)
#
#
# # wyr = "1+2+3+5"
# # liczby = []
# # operat = []
# # onp = []
# # for znak in wyr:
# #     if ord(znak) <= 57 and ord(znak) >= 48:
# #         liczby.append(znak)
# #     else:
# #         operat.append(znak)
# #     if len(liczby) == 2 :
# #         onp.append(operat[0])
# #         operat.pop(0)
# #         liczby.clear()
# #     elif len(operat):
# #         onp.append(operat[0])
# #         operat.pop(0)
# #         liczby.clear()
# #     print("ONP=", onp, "Liczby", liczby, "Operatorzy", operat)
# #
# # onp.append(operat[-1])
# #
# # print("ONP=",onp, "Liczby",liczby, "Operatorzy", operat)
#
#
#
# # wyr = "{[()]}"
# #
# # def spr(no, nz):
# #     if no == '(' and nz == ')':
# #         return True
# #     if no == '{' and nz == '}':
# #         return True
# #     if no == '[' and nz == ']':
# #         return True
# #     return False
# # def sprNawiasy(napis):
# #     listaNaw = []
# #     for i in napis:
# #         if i =='('or i == '{' or i == '[' :
# #             listaNaw.append(i)
# #         elif i ==')'or i == '}' or i == ']' :
# #             if spr(listaNaw[-1],i):
# #                 #print(listaNaw[-1],i)
# #                 listaNaw.pop()
# #     if len(listaNaw) == 0 :
# #         return True
# #     else:
# #         return False
# # print(sprNawiasy((wyr)))
#
# # def ONP(w) :
# #     stos = []
# #     stos.append('#')
# #     onp = ""
# #
# #     for i in range(len(w)) :
# #         if w[i]=='(' :
# #             stos.append('(')
# #             continue
# #         if w[i]==')':
# #             while stos[-1]!='(':
# #                 onp=onp+stos[-1]
# #                 stos.pop()
# #             stos.pop()
# #             continue
# #         if w[i]=='+' or w[i]=='-':
# #             while stos[-1]!='#' and stos[-1]!='(':
# #                 onp=onp+stos[-1]
# #                 stos.pop()
# #             stos.append(w[i])
# #             continue
# #         if w[i]=='*' or w[i]=='/':
# #             if stos[-1]=='*' or stos[-1]=='/':
# #                 onp=onp+stos[-1]
# #                 stos.pop()
# #             stos.append(w[i])
# #         else :
# #             onp=onp+w[i]
# #     while stos[-1] != '#':
# #         onp = onp + stos[-1]
# #         stos.pop()
# #     stos.pop()
# #     return onp
# #
# #
# #
# # if __name__ == '__main__':
# #     w = "(1+3)*6+(2-1)"
# #     print( ONP(w))
#
#
# # slw= {'Marcin': 123123123 , Marcin : 456456456}
# #
# # slw.update({'Mikolaj': 576378567})
# # y= input("Podaj imie: ")
# # x = int(input("Podaj numer: "))
# #
# # slw.update({y: x})
# #
# # del slw['Marcin']
# #
# # for i in slw:
# #     print(i , '-' , slw[i])
# # def licz():
# #     n=0.3333333333333333333
# #     return  n*3
# # if __name__ == '__name__':
# #     print(licz())
#
#
#
# import random
# iloscoczek = " "
# def rzut(x):
#     punkty = 100
#     for i in range(x):
#         iloscoczek = random.randint(1, 6)
#         if iloscoczek == 1:
#             punkty = 1
#             print("wypadło:", iloscoczek)
#             print("punkty:", punkty,'\n')
#         if iloscoczek == 2 or iloscoczek == 3:
#             punkty = punkty / 2
#             print("wypadło:", iloscoczek)
#             print("punkty:", punkty,'\n')
#         if iloscoczek == 4 or iloscoczek == 5:
#             punkty = punkty * 2
#             print("wypadło:", iloscoczek)
#             print("punkty:", punkty,'\n')
#         if iloscoczek == 100:
#             punkty = punkty
#             print("wypadło:", iloscoczek)
#             print("punkty:", punkty,'\n')
# rzut(3)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # x=3
# # listaarg = [3,2,1,-1,-2]
# # s=4
# # # 3*x^4+2*x^3+1*x^2+-1+-2*x^0
# # # 3*3*3*3*3+2*3*3*3+1*3*3+-1*3+-2*1
# # listaarg.reverse()
# # w=1
# # wielomian=listaarg[0]
# # print(wielomian)
# # for i in range(1,s+1):
# #     w*=x
# #     wielomian+=w*listaarg[i]
# #     print(wielomian)
# #
# #
# # napisz program ktory wczyta podstawy otengi oraz napis reprezentujacy wykladnik potengi w systemie binarnym a nastepnie wypisze wartosc potengi.Zastoj funkcje ktora byla na lekcji.
# # def potenga(podstawa, wykladnik):
# #     x=bin(podstawa**wykladnik)
# #     print(x)
# # print(potenga(2,3)
#
#
#
#
# # def alg(reszta)
# #     global nomin
# #     nomin=(500,200,100,50,20,10,5,2,1)
# #     i=0
# #     tablica=[]
# #     while reszta>0:
# #         if reszta>=nomin[i]:
# #             tablica.append(nomin[i])
# #             reszta-=nomin[i]
# #         else:
# #             i+=1
# #     return tablica
# #     t=alg(reszta)
# #     for i in nomin:
# #         if t.count(i):
# #             print(i,"=",t.count(i),"szt")
#
#
# # def bintodec(s):
# #     p=len(s)-1
# #     w=0
# #     for i in s:
# #         if i=='1':
# #             w=w+2**p
# #         p-=1
# #     return w
#

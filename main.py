# import xxxxxxxxxx from lol.py





# lista=[[],[]]
# wyr = '1 * 2 * (3 + 4)'
#
# for i in wyr:
#     if ord(i) <= 57 and ord(i) >= 48 :
#         lista[0].append(i)
#     else:
#         lista[1].append(i)
#
# print(lista)


# wyr = "1+2+3+5"
# liczby = []
# operat = []
# onp = []
# for znak in wyr:
#     if ord(znak) <= 57 and ord(znak) >= 48:
#         liczby.append(znak)
#     else:
#         operat.append(znak)
#     if len(liczby) == 2 :
#         onp.append(operat[0])
#         operat.pop(0)
#         liczby.clear()
#     elif len(operat):
#         onp.append(operat[0])
#         operat.pop(0)
#         liczby.clear()
#     print("ONP=", onp, "Liczby", liczby, "Operatorzy", operat)
#
# onp.append(operat[-1])
#
# print("ONP=",onp, "Liczby",liczby, "Operatorzy", operat)



# wyr = "{[()]}"
#
# def spr(no, nz):
#     if no == '(' and nz == ')':
#         return True
#     if no == '{' and nz == '}':
#         return True
#     if no == '[' and nz == ']':
#         return True
#     return False
# def sprNawiasy(napis):
#     listaNaw = []
#     for i in napis:
#         if i =='('or i == '{' or i == '[' :
#             listaNaw.append(i)
#         elif i ==')'or i == '}' or i == ']' :
#             if spr(listaNaw[-1],i):
#                 #print(listaNaw[-1],i)
#                 listaNaw.pop()
#     if len(listaNaw) == 0 :
#         return True
#     else:
#         return False
# print(sprNawiasy((wyr)))

# def ONP(w) :
#     stos = []
#     stos.append('#')
#     onp = ""
#
#     for i in range(len(w)) :
#         if w[i]=='(' :
#             stos.append('(')
#             continue
#         if w[i]==')':
#             while stos[-1]!='(':
#                 onp=onp+stos[-1]
#                 stos.pop()
#             stos.pop()
#             continue
#         if w[i]=='+' or w[i]=='-':
#             while stos[-1]!='#' and stos[-1]!='(':
#                 onp=onp+stos[-1]
#                 stos.pop()
#             stos.append(w[i])
#             continue
#         if w[i]=='*' or w[i]=='/':
#             if stos[-1]=='*' or stos[-1]=='/':
#                 onp=onp+stos[-1]
#                 stos.pop()
#             stos.append(w[i])
#         else :
#             onp=onp+w[i]
#     while stos[-1] != '#':
#         onp = onp + stos[-1]
#         stos.pop()
#     stos.pop()
#     return onp
#
#
#
# if __name__ == '__main__':
#     w = "(1+3)*6+(2-1)"
#     print( ONP(w))


# slw= {'Marcin': 123123123 , Marcin : 456456456}
#
# slw.update({'Mikolaj': 576378567})
# y= input("Podaj imie: ")
# x = int(input("Podaj numer: "))
#
# slw.update({y: x})
#
# del slw['Marcin']
#
# for i in slw:
#     print(i , '-' , slw[i])
# def licz():
#     n=0.3333333333333333333
#     return  n*3
# if __name__ == '__name__':
#     print(licz())



import random
iloscoczek = " "
def rzut(x):
    punkty = 100
    for i in range(x):
        iloscoczek = random.randint(1, 6)
        if iloscoczek == 1:
            punkty = 1
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
        if iloscoczek == 2 or iloscoczek == 3:
            punkty = punkty / 2
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
        if iloscoczek == 4 or iloscoczek == 5:
            punkty = punkty * 2
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
        if iloscoczek == 100:
            punkty = punkty
            print("wypadło:", iloscoczek)
            print("punkty:", punkty,'\n')
rzut(3)

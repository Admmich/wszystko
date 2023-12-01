# x=3
# listaarg = [3,2,1,-1,-2]
# s=4
# # 3*x^4+2*x^3+1*x^2+-1+-2*x^0
# # 3*3*3*3*3+2*3*3*3+1*3*3+-1*3+-2*1
# listaarg.reverse()
# w=1
# wielomian=listaarg[0]
# print(wielomian)
# for i in range(1,s+1):
#     w*=x
#     wielomian+=w*listaarg[i]
#     print(wielomian)
#
#
# napisz program ktory wczyta podstawy otengi oraz napis reprezentujacy wykladnik potengi w systemie binarnym a nastepnie wypisze wartosc potengi.Zastoj funkcje ktora byla na lekcji.
# def potenga(podstawa, wykladnik):
#     x=bin(podstawa**wykladnik)
#     print(x)
# print(potenga(2,3)




# def alg(reszta)
#     global nomin
#     nomin=(500,200,100,50,20,10,5,2,1)
#     i=0
#     tablica=[]
#     while reszta>0:
#         if reszta>=nomin[i]:
#             tablica.append(nomin[i])
#             reszta-=nomin[i]
#         else:
#             i+=1
#     return tablica
#     t=alg(reszta)
#     for i in nomin:
#         if t.count(i):
#             print(i,"=",t.count(i),"szt")


def bintodec(s):
    p=len(s)-1
    w=0
    for i in s:
        if i=='1':
            w=w+2**p
        p-=1
    return w
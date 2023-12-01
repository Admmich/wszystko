x=3
listaarg = [3,2,1,-1,-2]
s=4
# 3*x^4+2*x^3+1*x^2+-1+-2*x^0
# 3*3*3*3*3+2*3*3*3+1*3*3+-1*3+-2*1
listaarg.reverse()
w=1
wielomian=listaarg[0]
print(wielomian)
for i in range(1,s+1):
    w*=x
    wielomian+=w*listaarg[i]
    print(wielomian)
return wielomian


a=int(input("dari primul numar:"))
b=int(input("dati al doilea numar:"))
c=int(input("dati al treilea numar:"))
if a>0 and b>0 and c>0:
    if b>c:
        print(b)
        if c>b:
            print(c)
else:
    print(a+b)
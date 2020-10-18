a=int(input("dati prima nota:"))
b=int(input("dati a doua nota:"))
c=int(input("dati a treia nota:"))
if c>=8:
    print(a,b,c)
if c<8:
    if a>b:
        print(a)
        if b>a:
            print (b)

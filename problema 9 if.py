ba=int(input("bile mari albe:"))
br=int(input("bile mari rosii:"))
bv=int(input("bile mari verzi:"))
ma=int(input("bile mici albe:"))
mr=int(input("bile mici rosii:"))
mv=int(input("bile mici verzi:"))
t=ba+br+bv+ma+mr+mv
print ("in total sunt",t, "bile")
bt=ba+br+bv
mt=ma+mr+mv
if bt>mt:
    print ("sunt mai multe bile mari", bt)
else:
    print ("sunt mai multe bile mici" ,mt)
if ba+ma>br+mr and xa+ya>xv+yv:
    print("sunt mai multe albe",ba+ma)
if br+mr>ba+ma and br+mr>bv+mv:
    print("sunt mai multe rosii",br+mv)
if bv+mv>br+mr and bv+mv>ba+ma:
    print("sunt mai multe verzi",bv+mv)



n1=int(input('Numarul primului elev este: ')) 
p1=int(input('punctajul acestuia este: '))
n2=int(input('Numarul al doilea elev este: '))
p2=int(input('punctajul acestuia este: '))
n3=int(input('Numarul al treilea elev este: ')) 
p3=int(input('punctajul acestuia este: '))
if (p1>p2) and (p1>p3):
    print('Punctajul maxim îl are elevul ', n1)
if (p2>p1) and (p2>p3):
    print('Punctajul maxim îl are elevul ', n2)
else:
    print('Punctajul maxim îl are  elevul ', n3)

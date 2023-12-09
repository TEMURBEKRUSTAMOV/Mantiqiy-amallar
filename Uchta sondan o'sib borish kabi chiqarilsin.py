a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
if a<b<c:
    print(a)
    print(b)
    print(c)
if a<c<b:
    print(a)
    print(c)
    print(b)
elif c<a<b:
    print(c)
    print(a)
    print(b)
if b<a<c:
    print(b)
    print(a)
    print(c)
elif b<c<a:
    print(b)
    print(c)
    print(a)
    

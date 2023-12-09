a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
if a<b<c:
    print(c)
    print(b)
    print(a)
if a<c<b:
    print(b)
    print(c)
    print(a)
elif c<a<b:
    print(b)
    print(a)
    print(c)
if b<a<c:
    print(c)
    print(a)
    print(b)
elif b<c<a:
    print(a)
    print(c)
    print(b)
    

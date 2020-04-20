def cf(n):
    f=(9/5)*n +32
    return f

def fc(n):
    c=(5/9)*(n-32)
    return c

def ck(n):
    k=n+273.15
    return k

def kc(n):
    c=n-273.15
    return c

def fk(n):
    k=(n-32)*(5/9)+273.15
    return k

def kf(n):
    f=(9/5)*n-459.67
    return f


t=input("So, you want to convert temperatures do you?\nWell then, first thing we will do is figure out between which two scales we will be converting.\nIf you want to convert from celsius to fahrenheit, just type in 'a'. \nIf you want to convert from fahrenheit to celsius, just type in 'b'.\nIf you want to convert from celsius to kelvin, just type in 'c'.\nIf you want to convert from kelvin to celsius, just type in 'd'.\nIf you want to convert from fahrenheit to kelvin, just type in 'e'.\nIf you want to convert from kelvin to fahrenheit, just type in 'f'.: ")
n=float(input('Type in the initial temperature here: '))

if t=='a':
    x=cf(n)
    print("{}C is equal to {}F.".format(n,x))

elif t=='b':
    y=fc(n)
    print("{}F is equal to {}C.".format(n,y))

elif t=='c':
    z=ck(n)
    print("{}C is equal to {}K.".format(n,z))

elif t=='d':
    w=kc(n)
    print("{}K is equal to {}C.".format(n,w))

elif t=='e':
    s=fk(n)
    print("{}F is equal to {}K.".format(n,s))

elif t=='f':
    m=kf(n)
    print("{}K is equal to {}F.".format(n,m))
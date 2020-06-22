def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return 0,1
    x1,y1 = gcdExtended(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return x,y

a,b=map(int,input().split())
x,y=gcdExtended(a,b)
print(str(x)+" "+str(y))

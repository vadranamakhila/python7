a,b=map(int,raw_input().split())
def gcd(x,y):
    k=abs(x-y)
    if (x-y)==0:
        return y
    else:
        return gcd(k,min(x,y))
print gcd(a,b)

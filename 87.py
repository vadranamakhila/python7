m,n=map(int,raw_input().split())
def gcd(a,b):
    r=abs(a-b)
    if (a-b)==0:
        return n
    else:
        return gcd(r,min(a,b))
print gcd(m,n)

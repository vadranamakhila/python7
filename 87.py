c,d=map(int,raw_input().split())
def gcd(m,n):
    r=abs(m-n)
    if (m-n)==0:
        return n
    else:
        return gcd(r,min(m,n))
print gcd(c,d)

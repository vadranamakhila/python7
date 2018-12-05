p,q=map(int,raw_input().split())
if(p>q):
    min1=p
else:
    min1=q
while(1):
    if(min1%p==0 and min1%q==0):
        print(min1)
        break
    min1=min1+1

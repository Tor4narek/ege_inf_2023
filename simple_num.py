K = list(map(int,input().split()))
def IsPrime(x):
   d=2
   while d*d<=x:
     if x%d==0:
       return False
     d+=1
   return True
S = 0
for x in K:
    if IsPrime(x):
        S = S+x
print(S)
if IsPrime(S):
    print("Yes")
else: print("No")

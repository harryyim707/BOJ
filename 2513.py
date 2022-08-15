import sys
input=sys.stdin.readline
n,k,s=map(int,input().split())
a=[]
b=[]
for i in range(n):
  x,y=map(int,input().split())
  if x<s:
    a.append([x,y])
  elif s<x:
    b.append([s-(x-s),y])
a.sort()
b.sort()
def bus(c):
  B=0
  ans=0
  for x,y in c:
    if B>=y:
      B-=y
    else:
      y-=B
      z=y%k
      if z==0:
        B=0
        ans+=2*(s-x)*(y//k)
      else:
        B=k-z
        ans+=2*(s-x)*(y//k+1)
    print(x, y, z, ans, B)
  return ans
print(bus(a)+bus(b))
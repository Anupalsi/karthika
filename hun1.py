#anu
n=int(input())-1
l=list(map(int,input().split()))
s=0
l.sort()
for i in range(n,-1,-1):
	s=s*10+l[i]
print(s)

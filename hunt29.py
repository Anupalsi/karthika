#anu
n1=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(n1-1):
	for j in range(i,n1):
		c=l[i:j+1]
		p.append(sum(c))
print(max(p))

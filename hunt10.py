#anu
n,m=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))

f=0
for i in s:
	if i not in l:
		f=1
		break
if f==0:
	print('YES')
else:
	print('NO')
		

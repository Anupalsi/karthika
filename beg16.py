N,K=list(map(int,input().split()))
for i in range (N+1,K):
	for j in range(2,i):
		if(i%j==0):
			break
	else:
			print(i,end=" ")

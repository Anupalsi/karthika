#anu
n=int(input())-1
l=list(map(int,input().split()))
l=l[::-1]
for i in range(n):
    print(l[i],end='->')
print(l[n])  

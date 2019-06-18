#anu
num=int(input())
med=list(map(int,input().split()))
med.sort()
num1=med[int(num/2)]
print(num1)

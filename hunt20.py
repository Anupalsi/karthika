#anu
b,c=map(int,input().split())
sin=0
for i in range(b,c+1):
    a=bin(i)
    a=a[2:len(a)]
    a=a.count("1")
    c=0
    for i in range(1,a):
        if a%i==0:
            c=c+1
    if c==1:
        sin=sin+1
print(sin)

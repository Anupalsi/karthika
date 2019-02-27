a11,b=map(str,input().split())
#d=len(a11)-len(b)
#d=abs(d)
d=0
if len(a11)>len(b):
    mins=b
    maxs=a11
elif len(a11)<len(b):
    mins=a11
    maxs=b
else:
    mins=a11
    maxs=b
for i in range(0,len(mins)):
    if a11[i]==b[i]:
        continue
    else:
        d=d+abs(ord(a11[i])-ord(b[i]))
while(i+1<len(maxs)):
    d=d+ord(maxs[i+1])-96
    i=i+1
print(d)

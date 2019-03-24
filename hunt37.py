//anukarthika
s1=input()
s2=""
for i in range(len(s1)-1):
	s2=s2+s1[i]
s3=s2[::-1]
if s2==s3:
	print("YES")
else:
	print("NO")

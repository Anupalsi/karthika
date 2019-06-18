#anu
s=list(map(str,input()))
for i in range(len(s)):
  if s[i].islower()==True:
        s[i]=s[i].capitalize()
  else:
        s[i]=s[i].lower()
for i in range(len(s)): print(s[i],end="")

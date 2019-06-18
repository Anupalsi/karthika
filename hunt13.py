#anu
from itertools  import permutations

s=input()
n=len(s)
p=list(permutations(s))
rl=[]
r=""
for i in p:
    r=""
    for j in range(n):
        r+=i[j]
    if r not in rl:
        rl.append(r)
for i in rl:
    print(i)

#anu
A=input().split()
B=input().split()
C=input().split()
if (A[0]==B[0]==C[0] or A[1]==B[1]==C[1] or (A[0]==A[1] and B[0]==B[1] and C[0]==C[1])):
  print('yes')
else:
  print('no')

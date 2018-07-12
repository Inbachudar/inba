i=int(input())
n=int(input())
b=int(input())
if(i>n and i>b):
  print(i)
elif(i>n and i<b ):
  print(b)
elif(i<n and n>b):
  print(n)
elif(i<n and n<b):
  print(b)


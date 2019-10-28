# Write a program which display first 10 even numbers on screen.

def Num(x):
  i=1
  j=1
  while j<=x:
      if i%2 ==0:
          print(i,end=" ")
          j=j+1
      i=i+1

x=(int(input("Enter the number")))
Num(x)
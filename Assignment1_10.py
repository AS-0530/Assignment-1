# Write a program which accept name from user and display length of its name.


def len(x):
    j=0
    for i in x:
        j=j+1
    print("Length of string=",j)

x=input("Enter string")
len(x)
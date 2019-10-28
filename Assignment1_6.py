# Write a program which accept number from user and check whether that number is positive or
# negative or zero.


def ChkNum(x):

    if x>0:
        print("Number is Positive")
    elif x<0:
        print("Number is Negative")
    elif x==0:
        print("Number is Zero")

x=(int(input("Enter the number")))
ChkNum(x)

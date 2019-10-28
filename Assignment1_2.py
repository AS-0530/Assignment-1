# Write a program which contains one function named as ChkNum() which accept one parameter as number.
# If number is even then it should display “Even number” otherwise display “Odd number” on console.(


def ChkNum(x):

    if(x%2 ==0):
        print("Number is Even")
    else:
        print("Number is Odd")


x=(int(input("Enter the number")))
ChkNum(x)
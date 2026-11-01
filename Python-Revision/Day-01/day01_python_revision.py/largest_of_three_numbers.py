# largest fo three numbers 

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))

if (a > b and a > c):
    print(f"{a} is greatest among these threes .")
elif (b>c and b > a):
    print(f"{b} is greatest among these threes .")
else :
    print(f"{c} is greatest among these threes .")
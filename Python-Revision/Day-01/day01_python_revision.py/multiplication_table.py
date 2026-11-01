#  multiplication table of a number 

n = int(input("Enter the number :"))

print("table of ", n)

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")


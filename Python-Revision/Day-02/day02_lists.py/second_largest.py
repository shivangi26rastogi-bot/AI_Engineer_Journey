#  second largest distinct number 

num = [2,3,4,5,6,8,8,9,9]

largest = max(num)

new = []
for i in num :
    if i < largest :
        new.append(i)

print(max(new))
#  calculate average of a list 

list = [2,3,4,5,7,8]

sum = 0

for i in list:
    sum += i

avg = sum/len(list)

print("average of a list ", avg)

#  doing it using fucntion 

def avg(list):
    sum = 0

    for i in list:
        sum += i

    av = sum/len(list)

    return av

print(avg(list))
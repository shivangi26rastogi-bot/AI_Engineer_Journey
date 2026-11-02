# count how many positive and negative number in a list 

positive = 0
negative = 0

list = [-1,0,9,8,-3,-4,-5,8]

for i in list :
    if i < 0 :
        negative += 1
    else :
        positive += 1

print("positive :" , positive ," negative :", negative)
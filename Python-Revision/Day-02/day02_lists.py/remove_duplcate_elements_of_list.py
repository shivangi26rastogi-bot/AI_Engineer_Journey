# remove the duplicate elements of the list 

l = [2,2,33,5,57,8,9,9]

#  1st method 

new_list = list(set(l)) 
# order may be vary

print(new_list)

#  2nd method 

new = []
for i in l :
    if i not in new :
        new.append(i)

print(new)
    


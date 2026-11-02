#  using list comprehension method 
#  extracting even numbers from the list 

list = [2,4,5,6,7,8,9,34]

even = [i for i in list if i%2 == 0]

print(even)
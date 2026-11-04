#  check wheather a string is palindrome or not


string = "wow"

reverse = ""

for i in string:
    reverse = i +reverse

print(string == reverse)
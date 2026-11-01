#  count vowels in a string 

str = "hello dear  i am here . Belong FROM THE GUJRAT."

# str = str.lower()
count = 0

for i in str.lower():
    if(i == "a" or i == "i" or i == "o" or i == "u" or i == "e"):
        count += 1

print("total vowels ina string are ", count)



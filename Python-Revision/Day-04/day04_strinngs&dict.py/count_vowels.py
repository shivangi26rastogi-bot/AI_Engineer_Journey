# count the vowels in the string

string = "i love my india ."

vowels = "aeiou"

count = 0

for i in string.strip().lower():
    if(i in vowels):
        count+=1

print(count)
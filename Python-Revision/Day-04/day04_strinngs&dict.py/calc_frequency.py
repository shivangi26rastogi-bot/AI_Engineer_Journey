#  counting the frequency of each character using dictionary

text = "python programming"

frequency = {}

for i in text :
    if i in frequency :
        frequency[i] =+ 1
    else:
        frequency[i] = 1

print(frequency.items())
string = input("Type something here :  ")
print(string,"has:-")

letter = 0
word = 1

for i in string:
    letter = letter + 1
    if i in " ":
        word = word + 1
        letter = letter - 1

print(word,"words")
print(letter,"letters")
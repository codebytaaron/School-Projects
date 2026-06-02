text = input("Enter a word or sentence: ")

count = 0

for letter in text:
    if letter in "aeiou":
        count = count + 1

print("Number of vowels:", count)

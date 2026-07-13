string = input("Enter a string: ")

words = string.split()

max_count = 0
prominent_word = ""

for word in words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        prominent_word = word

print("Most prominent word:", prominent_word)
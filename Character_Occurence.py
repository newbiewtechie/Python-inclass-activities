# Character Occurence Activity
word = str(input("Enter a word: "))
char = str(input("Enter a character from this word: "))
i =0
count = 0
while (i <len(word)):
  if(word[i] == char):
    count= count+1
  i = i+1

print(char, "is appearing ", count, "times")

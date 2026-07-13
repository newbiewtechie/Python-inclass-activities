character = input("Enter a character: ")
if len(character) == 1:
    if (character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z'):
       print(f"'{character}' is an alphabet.")
    else:
        print(f"'{character}' is not an alphabet.")
else:
    print("Please enter only a single character.")
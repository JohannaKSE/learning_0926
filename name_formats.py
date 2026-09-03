name = input("Enter your name: ")
vowels = "aeiouAEIOU"

name_without_vowels = "".join(
    letter for letter in name if letter not in vowels
)
only_vowels = "".join(
    letter for letter in name if letter in vowels
)

print("All caps:", name.upper())
print("Lowercase:", name.lower())
print("Without vowels:", name_without_vowels)
print("Only vowels:", only_vowels)

team_name = "Data & AI Team at KSE Process Technology B.V"
vowels = "aeiouAEIOU"


def print_with_letter_count(label, text):
    """Print a version of the name and count only its alphabetic characters."""
    letter_count = sum(character.isalpha() for character in text)
    print(f"{label}: {text}")
    print(f"Letters printed: {letter_count}\n")


# Build both filtered versions once, then send every result through the same
# function so the letter count is always calculated and displayed consistently.
without_vowels = "".join(
    character for character in team_name if character not in vowels
)
only_vowels = "".join(
    character for character in team_name if character in vowels
)

print_with_letter_count("All caps", team_name.upper())
print_with_letter_count("Lowercase", team_name.lower())
print_with_letter_count("Without vowels", without_vowels)
print_with_letter_count("Only vowels", only_vowels)

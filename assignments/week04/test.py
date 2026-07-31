#what is your name?
#what text have 4 vowels?

name = input("What is your name? :")
letters = list(name)
vowels = "aeiouAEIOU"
vowel_count = sum(1 for letter in letters if letter in vowels)
print(f"Your name has {vowel_count} vowels.")

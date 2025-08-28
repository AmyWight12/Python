#   Scenario: redesign the previous lab and create a better, upgraded (pretty) vowel eater!
#   1. ask the user to enter a word;
#   2. use user_word = user_word.upper() to convert the word entered by the user to upper case;
#   3. use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#   4. assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.

user_word = input("Enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""

# each character of user_word will be stored in letter
for letter in user_word:
    if letter in ("A", "E", "I", "O", "U"):
        continue
    else:
        word_without_vowels = word_without_vowels + letter

print(word_without_vowels)
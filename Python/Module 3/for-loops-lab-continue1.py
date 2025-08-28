#   Scenario: The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
#   Can be used with while and for loops.
#   Your task here is very special: you must design a vowel eater! Write a program that uses:
#   - a for loop
#   - the concept of conditional execution (if-elif-else)
#   - the continue statement

#   1. ask the user to enter a word;
#   2. use user_word = user_word.upper() to convert the word entered by the user to upper case;
#   3. use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#   4. print the uneaten letters to the screen, each one of them on a separate line.

user_word = input("Enter a word: ").upper()

#letter is an empty var created that will store each character of user_word per interation
for letter in user_word:
    if letter in ("A", "E", "I", "O", "U"):
        continue
    else:
        print(letter)

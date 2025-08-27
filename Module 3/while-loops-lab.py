#   Scenario: A magician picked a secret number, it is hidden from the user. You have to guess it. The loop will run until you guess it.
#   Task:
#   1. ask a user to enter an integer number
#   2. use a while 
#   3. check whether the number is equal to the secret number picked by the magician.
#   4. if its not equal print "Ha ha! You're stuck in my loop!", if its equal print "Well done, muggle You are free now."

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
num = int(input("enter an integer number: "))

while (num != secret_number):
    print("Ha ha! You're stuck in my loop!")
    num = int(input("enter an integer number: "))
else:
    print("Well done, muggle You are free now.")
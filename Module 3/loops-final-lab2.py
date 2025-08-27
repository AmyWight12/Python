#   Scenario:In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (it still remains unproven) which can be described in the following way:
#   1. take any non-negative and non-zero integer number and name it c0;
#   2. if it's even, evaluate a new c0 as c0 ÷ 2;
#   3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
#   4. if c0 ≠ 1, skip to point 2.
#   The hypothesis says that regardless of the initial value of c0, it will always go to 1.

#   Objectives: Familiarize the student with:
#   using the while loop;
#   converting verbally defined loops into actual Python code.


c0 = int(input("Enter an integer number: "))
counter = 0

while (c0 != 1):
    if (c0 % 2 == 0):
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    counter += 1
    print(c0)

print("steps: ", counter)
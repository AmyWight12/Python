# step 1: create an empty list names beatles
beatles = []
print("Step 1:", beatles)

# step 2: add the following members to the end of the list (John Lennon, Paul McCartney, George Harrison)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3: use a loop to prompt users to add the following members to the list(Stu Sutcliffe, and Pete Best)
for i in range(2):
    member = input("Add one of the following members (Stu Sutcliffe and Pete Best): ")
    beatles.append(member)
print("Step 3:", beatles)

# step 4: remove Stu Sutcliffe and Pete Best from the list
del beatles[-1]
del beatles[-2]
print("Step 4:", beatles)

# step 5: add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
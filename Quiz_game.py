print("Welcome to my computer Quiz!")

playing = input("Do you want to play? (yes/no) ")
# print(playing)
# .lower() convert every thing in lower case

if playing.lower() != "yes":
    print("This Quiz is over")
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")


print("You got " + str((score*4) / 400) + "%")


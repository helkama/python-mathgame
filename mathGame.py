import random
import time
points = 0

print("This is a math game. Solve the math problem.")

st = time.time()
while True:

    num1 = random.randrange(0,10)
    num2 = random.randrange(0,10)
    print("Solve",num1,"*",num2)
    answer = num1 * num2
    guess = int(input("Answer: "))



    if guess == answer:
        print("Correct answer!\n")
        points += 1
    elif guess != answer:
        print("Wrong answer! :(\n")
        break
        
et = time.time()
totalTime = et - st

print("You got",str(points),"points!")
print("Time taken:",str(round(totalTime,2)),"seconds")

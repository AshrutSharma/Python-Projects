import random
Ans = random.randint(0, 10)
Guess = input("Guess the random number between 1 and 10 : ")
Score = 10

while not Guess.isdigit():
    Guess = input("Enter a valid number : ")

if Guess.isdigit():
    Guess = int(Guess)

while Guess > 10 or Guess < 0:
    Guess = int(input("Enter a valid number : "))

while Guess != Ans:
    if Guess - 1 == Ans or Guess + 1 == Ans:
        Guess = int(input("You were very close : "))
        Score -= 2
    elif Guess - 2 == Ans or Guess + 2 == Ans:
        Guess = int(input("You were close : "))
        Score -= 2
    elif Guess - 3 == Ans or Guess + 3 == Ans:
        Guess = int(input("Not the right number, think something else : "))
        Score -= 2
    elif Guess - 4 == Ans or Guess + 4 == Ans:
        Guess = int(input("You were quite far from the answer : "))
        Score -= 2
    else:
        Guess = int(input("You were nowhere near the answer : "))
        Score -= 2
    if Score == 0:
        print("You lose")
        break

if Score > 0:
    print("You were correct!")

print("Your score : " + str(Score))

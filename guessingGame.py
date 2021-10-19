import random
print("Number Game")
number = random.randint(1,9)
chan = 0
print("Guess between 1 to 9")
while chan < 5:
    guess = int(input("Enter Your Guess"))
    if guess == number:
        print("Cong!!")
        break
    elif guess < number:
        print("Higher",guess)
    else:
        print("Lower",guess)
    chan+=1
if not chan < 5:
    print("u Lose",number)
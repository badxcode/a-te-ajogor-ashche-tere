i = 1
while i<=10:
    print(i)
    i = i+1

i = 1
while i<=5:
    print("*" * i)
    i += 1

target_number = 6
guess_limit = 3
i = 0
while i<guess_limit:
    i = i+1
    users_guess =int(input("Guess: "))
    if users_guess == target_number:
       print("You won")
       break
else:
    print("You lose")
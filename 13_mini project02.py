secret = 7
guess = int(input("Enter the number:"))
while guess != secret:
    if guess < secret:
        print("Too low!")
    elif guess > secret:
         print("Too high!")
    guess = int(input("Wrong! Enter the number:"))
else:
    print("correct")


#Revised version
secret = 7
attempts = 0
guess = int(input("Enter the number:"))
while True:
    attempts +=1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("correct")
        print("You guesses it in", attempts, "attempts.")
        break 
    guess = int(input("Wrong! Enter the number:"))
    
    

    
    


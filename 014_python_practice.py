# == STUDENT PORTAL ==
name = input("enter your name:")
age = int(input('enter your age:'))
username = input("enter your username:")
marks = int(input("enter your marks:"))
while len(username) <5 or " " in username:
    print("username must be at least 5 characters long without spaces")
    username = input("enter your username:")
print("Welcome to student portal",name)
has_digit = False
for letter in username:
    if letter.isdigit():
        has_digit = True
while has_digit == False:
    print("username must contain atleast one digit")
    username = input("enter your username:")
    has_digit = False
    for letter in username:
        if letter.isdigit():
            has_digit = True
print("username is valid")
if age >=18 and marks >=50:
    print("Eligible")
else:
    print("Not eligible")
if marks >= 90:
    print("Excellent")
elif marks > 75:
    print("Good")
elif marks >= 50:
    print("You can do better")

# == EXAM ELIGIBILITY CHECKER ==
age = int(input('enter your age:'))
attendence = float(input("enter your attendence percentage:"))
marks = int(input("enter your marks:"))
if marks >= 50:
    if attendence >= 75:
        if age >=18:
            print("Eligible for exam")
        else:
            print("Not eligible for exam due to age")
    else:
        print("Not eliglible for exam due to low attendence")
else:
    print("Not eligible for exam due to low marks")


# == ATM lOGIN SYSTEM ==
pin = int(input("enter your pin:"))
attempts = 3
while attempts >0:
    if pin == 2568:
        print("Access granted")
        break
    else:
        attempts -=1
        print("Incorrect password. You have",attempts,"attempts left")
        pin = int(input("enter your pin:"))
if attempts == 1:
    print('Access denied. you have exceeded the maximum number of attempts')
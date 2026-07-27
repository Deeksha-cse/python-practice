#  REVISION SESSION 

#practice q1

for name in range(5):
    print("Deeksha")

count = 1
while count <= 5:
    print('Deeksha')
    count +=1


#practice q2

for i in range(10,21):
    print(i)

count = 10
while count <=20:
    print(count)
    count +=1

#practice q3

for i in range(2,21,2):
    print(i)

count = 2
while count <=20:
    print(count)
    count +=2



#practice q4

for i in range(20,0,-1):
    print(i)

count = 20
while count >=2:
    print(count)
    count -=2

#practice q5
count = 1 
while count <=5:
    print(count)
    count +=1


#practice q6
#ask a user for a number and and classify as true or false using while loop 
#let's understand the programming 
choice = "yes"
#we created a variable and stored yes in it
while choice  == "yes":
    number = int(input("enter your number:"))
    if number %2 == 0:
        print("even")
    else:
        print("odd")
    choice = input("check a another number: (yes/no)")

#if choice is yes then the loop starts 
#this print if the number is whether even or odd
#if the choice is no then the loop stops


#practice q7

password = input("enter your password:")
while password != "python123":
    password = input("Enter your password:")
print("access granted")

#practice q9
for row in range(5):
    for col in range (row+1):
        print("*", end="")
        print()


#practice q10
count = 5
while count >0:
    print(count)
    count -=1



#practice q11
sentence = input("enter a sentence:")
print(sentence.count(" "))

#practice q12
username = input("enter your name :")
if " " in username:
    print("invalid username")
else:
    print("valid username")


#practice q12
word = input("enter a word:")
print(word.upper())
print(word.lower())
print(word.title())
print(word.count("a"))


#practice q13
choice = "yes"
while choice =="yes":
name = input("enter your name:")
age = int(input("enter your age:"))
marks = int(input("enter your marks:"))
password = input("enter your password:")
while password != "python123":
    password = input("password is incorrect")
print(name. upper())
if marks >= 90:
    print("excellent")
else:
    print("keep working hard")
if age < 18:
    print("Minor")
else:
    print("Adult")
for num in range(1,11):
    print(age "x",num,"=",age * num)
choice = input("do you want to run the program again : (yes/no)")
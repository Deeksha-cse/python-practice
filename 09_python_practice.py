#PYTHON LOOPS

#What is Loop?
#a loop is a way to repeat the same block of code multiple times without writing the code again
#imagine u have print Welcome! 100 times
print("Welcome!") 
#u can't write this 100 times
#this is where loops are useful

#Why do we need loops?
#sending a message to 100 users
#checking every student in a class
#reading everyline in a file
#printing multiplication table
#processing every image in folder
#asking the user again if they enter invalid input

#Example in real life 

#Instagram Feed
#load post > show posts > user scrolls > load next posts > repeat

# TYPES OF LOOPS

#1. 'while' loop
#use while loop when you don't know in advance how many times the code should repeat 
 
 #the loop continues as long as the condition is true

 #syntax
 #while condition:
 #     statement
 
count = 1
while count <=5:
    print(count)
    count += 1

# count = 1
#variable name count is created aand starts with value 1 

#while count <=5:
#python asks is the count less than or equal to 5?
#if the answer is True, it enters the loop

#count += 1
#this shorthanded  for count = count + 1
# this is a very important step let's trace it
count = 1
#1<5
print(count)
1
count = 1+1
count = 2
#2<5
print(count)
2
count = 2+1
count = 3
#this continues till the condition satisfy =5
#if
count = 6
#6>5
#SO that loop stops

#start
#check condition
#True?
#_____Yes_________
#execute code     |
#update variable  |
#_____Back________|
#False?
#stop

#INFINTE LOOP

#if the condition never becoms False, the loop never stops
#while True:
#    print("Hello")
#since True is always True the condition never stops

#count = 1 
#while count <=5:
 #   print(count)

#output is 1 1 1 1
#because count never changes 

pin = int(input("Enter your pin:"))
while pin != 1981:
    pin = input("Enter your pin:")
print("Acess denied")

count = 1
while count <= 3:
    print("Deeksha")
    count +=1

#output 
#Deeksha
#Deeksha
#Deeksha
#eventhough text doesn't change, the counter controls how many times it prints

secret = int(input("enter your secret number:"))
while secret != 8:
    secret = int(input("Wrong! Enter your secret number:"))
print("access allowed")

#one important concept 
#if asks : should i do this?
#while asks: should i do this again?


#TYPE 2 
#'for' loop 
# a for loop repeats code a specific number of times

#while vs for
#using while 
count = 1
while count <= 5:
    print(count)
    count +=1

#steps 
#creates a variable named count 
#checks the condition 
#increase the count

#using for
for number in range(0,5):
    print(number)

#python automatically 
#creates a variable 
#changes its value
#stops the loop

#syntax 
#for variable in range():
#      statement


#let's understand very word
#for
#loop starts

#number 
#here it is called loop variable
#python stores in it automatically as
number = 1
number =2
number = 3
#until it reaches the end
#you don't need write 
count +=1
#python already does it

#soo basically while is used if we are not certain about when the loop is going to end
#forloop is used when we are certain about it

#UNDERSTANDING range()
range(5)
#range(stop)
#example
for number in  range(5):
    print(number)

#output
0
1
2
3
4
#5 is not printed

for number in range(0,5):
    print(number)
#range(start,stop)
#start is included stop is not

for number in range(0,6,2):
    print(number)
#range(start,stop,step)

for number in range(5,0,-1):
    print(number)
#it moves back wards
#output is 
#5
#4
#3
#2
#1


#mini challenge1

#using for loop
for number in range(1,21):
    print(number)
#using while loop
count =1
while count <=20:
    print(count)
    count += 1

#mini challenge 2
for number in range(1,16,2):
    print(number)

#mini challenge 3
for name in range(7):
    print("Deeksha")

count = 1
while count <=7:
    print("Deeksha")
    count +=1

#mini challenge 4
number = 1
while number <=10:
    print("9x",number,"=", 9*number)
    number +=1

for number in range(1,11):
    print("9x", number, "=", 9*number)

#mini challenge 5
for number in range(20,0,-1):
    print(number)

#more about loop variables
#imagine they are 5 students
#Deeksha
#spandana
#akshara
#jagruthy
#sahiti

#you tell your assistant
#"go to each student one by one"
current_student = "Deeksha"
#the assistant is changing the current student ,that "current_student" is a loop variable

#coders actually use "i" because i represents index or iteration but any meaning ful name works too
#logical operators



#logical operators are used to combine two or more conditions into single condition
#think of them as words that connect ideas


#Real life example
#I can go to ladakh if i score well in this semester and my parents are free
#here and is combining both sentences
#both must be true
#python uses logical operators to express this


#types of logical operators

#and- both must be true
#or-at least one condition must be true
#not- reverse True to False False to True

#The 'and' operator
#definition
#the 'and' operator returns True only if every condition is True

username = input("enter your name:").strip().lower()
password = input("enter your password:")
if username == "deeksha" and password =="deeksha2009":
    print("access allowed")
else:
    print("access denied")


#here more about .lower()
username = input("enter your name:").lower()
username = "Deeksha"
#"deeksha"


#here more about .strip()
#this removes the whitespace from the beginning and end of a string
#it does not the spaces in middle of the words
username = input("enter your name:")
#the user types "Deeksha "
username ="Deeksha "
#python stores in it
if username == "Deeksha":
    print("correct")
else:
    print("wrong")
#output is definitely wrong because there a extra space 
# so this is where strip helps
#  lstrip deletes the left space and rstrip deletes te right space
#strip deletes the spaces in both ends

username = "Deeksha " .rstrip()
if username =="Deeksha":
    print("correct")
else:
    print("wrong")
    
#other example for "and " operator
age = 20
if age >=18 and age <=35:
    print("eligible")
else:
    print("not eligible")

#practice q1
marks = int(input("enter your marks:"))
attendance = float(input("enter your percentage"))
if marks >= 90 and attendance >=85:
    print("eligible for scholarship")
else:
    print("scholarship denied")





# The "or" operator
#the "or" operator returns True  if at least one condition is True

day = input("what day is it:").strip().lower()
if day =="saturday" or day =="sunday":
    print("yayy! it's weekend")
else:
    print("weekday")


#example 2
rank = int(input("enter your met rank:"))
percentage = float(input("enter your percentage:"))
if  rank <= 5000 or percentage >= 98:
    print('eligible')
else:
    print("not eligible")


#The "not" operator
#"not" reverse the boolean value

#True > False
#False > True

logged_in = False
if not logged_in:
    print("please login")


#python checks it as following
logged_in = False
not False
True
print("please login")

#example 2
is_raining = True
if not is_raining:
    print("go outside")
else:
    print("stay at home")


#operator precedence

#operator precedence is one of the most important concepts in python 
#think of it like BODMAS in maths
#operator precedence is the order in which python evalutes operators

#this the order in which python evaluate operators

1 ()
2 #not
3 #and
4 #or
 
#example1
result = (5+3)*3
print(result)
#output 24

#example2
print(not False and True)
#first
#not False
True
#True and True
True

#example 3
print(True or False and False)
#False and False
False
#True or False
True

#example4
print(True and False or True)
#True and False
False
#False or True
True

#sooo basically
not True
#False
not False
#True
True and True
#True
True and False
#False
False and False
#False
False and True
#False
True or False
#True
False or True
#True
True or True
#True
False or False
#False



#practice q1
balance = int(input("enter your balance:"))
password = input("enter your password:")
if balance >=5000 and password == "motupatlu123":
    print("withdraw your money")
elif balance >= 5000 and password!= "motupatlu123":
    print("incorrect password")
else:
    print("insufficient balance")


#practice2
age = int(input("enter your age:"))
answer = input("do you have driving licence: (yes/no)").lower().strip()
if age >= 18 and answer =="yes":
    print("you can drive")
else:
    print("you are not eligible")

#practiceq3
number = int(input("enter your number:"))
if number < 0:
    print("negative")
elif number >0:
    print("positive")
else:
    print("neither negative nor positive")


#practice q4
username = input("enter your name:").lower().strip()
password = int(input("enter your password:"))
if username == "deeksha":
    if password == 2009:
        print("login successful")
    else:
        print("incorrect password")
else:
    print("invalid username")


answer = input("got adimmision in the college?:  (yes/no)").lower().strip()
verified = input("are your documents verified?: (yes/no)").lower().strip()
if answer == "yes":
    if verified == "yes":
        print("Welcome!")
    else:
        print("your documents are not verifies")
else:
    print("sry! you did get a admission")
 


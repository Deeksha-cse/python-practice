print ("Learning python is fun!")
#this comment python doesn't execute the code in comments
print ("hello world")
#this is my first python program without copying the code from the internet
print ("welcome to python programming!")
#print() this appears in the output but it is not printed because it is commented out 
#you can print varaibles
print(10)
print (1.9)
#you can print
print('Deeksha')
#parenthese() 
print ("hello world")
#here print is a function () contains what you want to print 
#quotations create a string (text) and text is printed in the output
print("India is awesome!")
print('india is awesome!')
#both are correct and will give the same output
#if you dont give quotations python thinks its a variable and will give an error
#variables are used to store data 
name = 'deeksha'
age = 17 
print (age)
#here age and name are variables and 17 and 'deeksha' are the values stored in them
name = 'DEEKSHA'
age = 17 
college = "mahe"
print (name)
print (age)
print (college)
#= is used to store the value in the variable
age = 17
x = 10
# = is not equal to in maths
# correct thinking is 10 stored in x




# variable naming rules
# start with letter or _
# can contain letters, numbers and _
# cannot start with a number 
# no spaces in variable names


# not allowed 

# 2age = 17
# my age = 17
# class = 10 (keyword)


# allowed 
my_age = 17
_age = 20
my_class = 10



#data types in python
#1. integer (int) - whole numbers 
age = 17
#2. float - decimal numbers
height = 5.9
# string (str) - text 
name = 'python' 
# boolean (bool) - true or false
has_passed = True


# heres about boolen data type 
#boolen data type has only True or Fales no other third party
# True or False also means on or off and yes or no 
# 1. is_student =
# this is a variable that can be either True or False depending on what you want to store in it 


#here 
is_student = True
#means the person is a student 


# examples 
is_logged_in = False
is_admin = True
is_teacher = False
is_raining = True
is_dark = False
is_open = True
has_money = True
can_vote = True
 # differences 
is_student = True
print(is_student)
#gives output True 
print(type(is_student))
#gives output <class 'bool'>
#this is boolean data type

#boolean vs string
is_student = True
is_student = "True"
print(type(True))
print(type("True"))
#output
#<class 'bool'>
#<class 'str'>

#where use these boolean data types
is_student = True
if is_student:
    print('student discount is applied')



#input function in python 

#input() function is used to take input from the User
# witgout input the program always take fixed values 
#for example
name = "deeksha"
print(name)
# the out put is deeksha not matter who ever runs it

name = input("enter your name: ")
print ("Hi",name)
# now the name changes for person to person same like the way chatgpt ask for our name

#how does the python excute input is
name = input("enter your name: ")
# the screen shows enter your name:
# the user type "Deeksha" and python receives it
# python stores in it as 
name = 'Deeksha'
print(name)
# out put is Deeksha 




age = input("what is your age?:")
print("next year you will be", age + 1 )
# out put be like "age" + 1 which is not possible so syntax erro
# this is beacuse python does not your intention of whether your giving int , float, str
# so it safely stores in str

# to correct this
age = int(input("enter your age: "))
print("next year you will be" , age + 1 )

weight = float(input("what is your weight?:  53.5"))
print("your weight is", weight, "kg")
#these int and float are used to convert the input into integer and float data types respectively
#otherwise the input is taken as string data type

quote = input("Enter your favourite quote:  ")
print("your favourite quote is", quote)

num1 = int(input("enter first number: "))
num2 = int(input("enter second number:" ))
print(num1 + num2)
print(num2-num1)

print("10" + "20")
#output is 1020
print("10" +str(20))
#output is 1020
print(10 + int(20))
#output is 30


#User types
#18
#↓
input()
#↓
#"18"
#↓
#int("18")
#↓
#18
#↓
#18 + 5
#↓
#23

#operators
a=3
b=2
print(a+b)
print(a-b)
print(a*b)#multiplication
print(a/b)#division
print(a%b)#remainder
print(a**b)#power
print(a//b)#floor division
#answers
#1. 5
#2. 1
#3. 6
#4. 1.5
#5. 1
#6. 9 3 power of 2 is 9
#7. 1 floor division means the answer is rounded down to the nearest whole number


#comparison operators
a=3
b=2
print(a==b)#equal to
#output is False because 3 is not equal to 2
print(a!=b)#not equal to
#output is true beacause 3 is not equal to 2
print(a>b)#a is greater than b
#output is true
print(a<b)
#false
print(18>=18)#greater than or equals to
#true








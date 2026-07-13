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
print("India is awesome!")or
print ('india is awesome!')
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
#start with letter or _
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
# True or False also means on or off and 
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





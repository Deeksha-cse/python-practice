#here more about bool data type



print(bool(0))
#output is False
print(bool("0"))
#output is True because this is quoted
# this both are completely different 
#zero indicates nothing so in bolean expression nothing means False
print(bool(-0.14))
#out put is True
#-0.14 is some value so the ouput is True
print(bool(1))
#output is True
print(bool(False))
#out put is False 
# as long as the str is non empty the output is True
print(bool("False"))
#output is True 
#False > something exists > True 
print(bool(""))
#output is False
#""> represents nothing > False
print(bool(" "))
#output is True
# " " > something exists > True
print(bool(0.4))
#output is True

print(bool(None))
#output is False
print(bool())
#output False
print(bool(1))
#output is True


# why bool is useful 
#Imagine the login system for any website
username = input("Enter your name: ")
# if the user click enter without  typing the username 
# python stores it as 
username = ""
print(bool(username))
#output is False
#other wise
#if the user type "Deeksha"
#the python stores it as
username = "Deeksha"
print(bool(username ))
#output is True 



#why input and bool can be misleading
#suppose 
light_on = bool(input(is_light_on))
#if the user types False
light_on = "False"
#python stores it
print(light_on)
#this is what happens next 
#input returns a string
"False"
#next
bool("False")
#output is True

username = input("enter your name:  ")
if bool(username):
    print('WELCOME!')
else:
    print("please enter your name: ")


# running my own login system

name = input ("enter your name:"  )
if bool(name):
    print("Thank you for visting our website")
else: 
    print("kindly enter your name")

age = int(input("Enter your age:"   ))
if age > 0:
    print("Thank you")
else:
    print("Age is required")

college = input("Name of your college: ")
if college:
     print("Thank you so much for cooperating with us")
else:
    print("Please enter the name of your college")


#comparison operators also come in bool data type

age = 17
print(age == 17)#True
print(age != 16)#true
print(age > 15)#True
print(age >= 17)#True


marks = int(input("Enter your marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Better luck next time")
  


password = input("Enter your password: ")
if bool(password):
    print("done and dusted")
else:
    print("kindly enter the password")


age = int(input("Please enter your age: "))
if age >= 18:
    print("your are an  adult")
else:
    print("access denied.You must be 18 years old")

Temparature = float(input("Enter your body temparature: "))
if Temparature < 38:
    print("you're perfectly alright")
else:
    print("take care of your self")

age = int(input("Enter your age:"))
if age < 13:
    print("you're a child")
elif age < 20:
    print("you're a teen")
else:
    print("you're an adult")










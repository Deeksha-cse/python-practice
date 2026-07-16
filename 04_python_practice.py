#here is more about elif 
#elif means if the previous condition is check this



# if condition1
#code runs if the condition1 is True

# elif condition2
#code runs if the the condition1 is False and condition2 is True

#else 
#code runs if all the conditions are False

# here is the example if use only if
age = 9 
if age <13:
    print("child")
if age <20:
    print("teenager")
if age >=20:
    print("adult")

#output 
#child
#teenager
# this is because python checks every if seperately



#using elif 
age = 9 
if age <13:
    print("child")
elif age <20:
    print("teenager")
else:
    print("adult")
#output
#child


marks = int(input("Enter your marks:"))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")




# practice q2
password = input("Enter your password:")
if len(password) <6:
    print("weak password")
elif len(password) < 10:
    print("medium password")
else:
    print("strong password")


#practice q3
signal = input("Enter signal:").lower()
if signal == "red":
    print("stop")
elif signal == "yellow":
    print("Get ready")
elif signal == "green":
    print("GO")
else:
    print("invalid signal")


#practice q4
balance = float(input("Enter your bank balance:"))
if balance <=100000:
    print("basic")
elif balance <=250000:
    print("silver")
elif balance <=500000:
    print("gold")
else:
    print("premium")




#practice q5
name = input("Enter your name:")
marks = int(input("enter your marks:"))
print("Name is:", name)
if marks >=90:
    print("Grade A")
    print("Pass")
    print("Excellent Work")
elif marks >=75:
    print("Grade B")
    print("Pass")
    print("keep it up")
elif marks >=50:
    print("Grade C")
    print("Pass")
    print("Do much better next time")
else:
    print("Fail")
    print("Work hard next time")


#practice q6
username = input("enter your name:").lower()
password = input("enter your password:")
if username == "deeksha":
   if password == "deeksha2009":
    print("login successful")
else:
    print("Invalid password or username")




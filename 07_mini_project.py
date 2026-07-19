#PROJECT: SMART USERNAME

username = input("enter your name:").lower().strip()
if len(username) >=5:
    if " " not in username:
        if username.startswith("hello"):
            print("valid username")
        else:
            print("username must start with hello")
    else:
        print("too many spaces")
else:
    print("username is too short")


# PROJECT: FILE VALIDATION
file = input("enter the name of the python file").lower().strip()
if file.endswith(".py"):
    if "python" in file:
        new_file = file.replace("python","java")
        print("new file is:",new_file)
        print("file is valid")
    else:
        print("filename must contain the word'python'")
else:
    print("file name must end with '.py'")


#PROJECT: STUDENT ID CARD
name = input("enter your name:")
college = input("enter the college name:")
branch = input("enter your department")
semester = int(input("enter your semester"))
print("Name:",name)
print("college:", college)
print("branch:",branch)
print("semester:", semester)
print("Welcome")


#LOGIN SYSTEM 2.0
username = input("enter your name:").lower().strip()
password = input("enter your password")
if len(username) >=10:
    if len(password) >=8:
        if "@" in password:
            if " " not in username:
                print("login successful")
            else:
                print("username have too many spaces")
        else:
            print("invalid password")
    else:
        print("invalid password")
else:
    print("username is too short")


#RESUME BUILDER

name = input("enter your name:").strip().title()
age =int(input("enter your age:"))
skills = input("enter your skills:")
dream_company = input("where do you want to work:").strip().title()
print("Myself",name)
print("I'm", age, "years old")
print("I'm good at", skills)
print("I wish I could work at", dream_company)


        


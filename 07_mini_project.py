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


        


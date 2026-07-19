#username validator
username = input("enter your name:").lower().strip()
if len(username) >= 5:
    if " " not in username:
        print("valid username")
    else:
        print("username has too many spaces")
else:
    print("username is too short")


#practice q2
file = input("enter the name of the file:")
if len(file) >=6:
    if " " not in file:
        if file.endswith(".py"):
            print("valid file name")
        else:
            print("file must end with .py")
    else:
        print("file name has too many spaces")
else:
    print("file name is too short")



#practice q3
word = input("enter the word:").lower()
print(word.count("a"))
if "python" in word:
    print("invalid word")
print(word.find("e"))
if "ai"in word:
    print("valid text")


#practice q4
sentence = input("enter the sentence:").lower()
if "deeksha" in sentence:
    print(sentence.replace("deeksha","riya"))
else:
    print("name not found")




#practice q5
gmail = input("enter your gmail:")
if gmail.endswith("@gmail.com"):
    print("valid gmail address")
else:
    print("invalid gmail")


#practice q6
password = input("enter your password:")
if " " not in password:
    print("valid password")
else:
    print("invalid password")


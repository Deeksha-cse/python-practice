#PYTHON MEGA REVISION CHALLENGE
#PART 1
username = input("enter your username:").lower().strip()
password = input("enter your password:").strip()
login ="no"
if bool(username) and bool(password):
    if " " not in username :
        if len(password)>=6:
            print("login successful")
            login = "yes"
        else:
            print("password is too short")
    else:
        print("username has too many spaces")
else:
    print("username or password cannot be empty")

while login =="yes":
    name = input("enter your name:")
    age = int(input("enter your age:"))
    college = input("enter your college name:")
    number_subjects = int(input("enter the number of subjects:"))
    while number_subjects >0:
        marks = int(input("enter your marks:"))
        if marks >=90:
            print("excellent")
            print("grade:A")
        elif marks >=80:
            print("very good")
            print("grade:B")
        elif marks >=70:
            print("good")
            print("grade:C")
        else:
            print("work hard")
            print("grade:D")
        number_subjects -=1
    if number_subjects == 0:
        print("you have entered all the subjects")
        login = "no"
        
        
username = input("enter your username").strip()
password = input("enter your password").strip()
if bool(username):
    if " " not in username:
        if username.isalpha():
            if "admin" not in username:
                if len(password) >=8:
                    print("login successful")
                    login = "yes"
                else:
                    print("password is too short")
            else:
                print("username cannot contain 'admin'")
        else:
            print("username must be alphabetic")
    else:
         print("username cannot contain spaces")
else:
    print("username is required")
    login = "no"
while login == "yes":
    print("welcome to student portal")
    name = input("enter your name:").strip()
    age = int(input("enter your age:"))
    college = input("enter the name of the college:").strip()
    max_classes = int(input("enter the maximum number of classes:"))
    attended = int(input("enter the number of classes attended:"))
    attendence_percentage = (attended / max_classes) * 100
    print("----STUDENT DETAILS----")
    print("NAME:", name)
    print("AGE:", age)
    print("COLLEGE:",college)
    print("ATTENDANCE PERCENTAGE:", attendence_percentage)
    if attendence_percentage <75:
        print("you're not eligible to use the student portal")
        break
    while attendence_percentage >= 75:
        choice ="yes"
        subjects = input("enter the subjects seperated by coma:").strip().split(",")
    #text = "deeksha ,18, cse ,mahe"
    #using split function to split the text into a list 
    #text.split(",")
    #output is 'deeksha', "18","cse","mahe"
    #text.split(",")[0] will give the first element of the list which is deeksha
    #text.split(" ")
    #output is "deeksha" "18" "cse" "mahe"
    #text.split("-")
    #output is "deeksha"-"18"-"cse"-"mahe"
        for subject in subjects:
            marks = int(input("enter the marks of the subject:"))
            print(subject + ":" + str(marks))
            if marks >=90:
                print("excellent")
                print("Grade A")
            elif marks >=80:
                print("very good")
                print("Grade B")
            elif marks >=70:
                print("good")
                print("Grade C")
            else:
                print("work hard")
                print("Grade D")
        hours_studied = int(input("enter the number of hours studied:"))
        if hours_studied >=5:
            print("excellent")
        elif hours_studied >=3 and hours_studied <5:
            print("good")
        elif hours_studied >=1 and hours_studied <=3:
            print("keep going")
        else:
            print("Bro!! study more")
        choice = input("do you want to continue>(yes/no):").lower().strip()
        if choice =="no":
            print("Thank you for using the student portal")
            login = "no"
            break
            

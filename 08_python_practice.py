#MOVIE TICKET CHECKER

age = int(input("enter your age:"))
if age <5:
    print("Ticket is Free")
elif age >=5 and age <18:
    print("Child Ticket")
elif age >=18 and age <=59:
    print("Adult Ticket")
else:
    print("Senior Ticket")


#WEATHER ADVISOR

is_raining = input("Is it raining?:  (yes/no)").lower().strip()
umbrella = input("Do you have an umbrella: (yes/no)").lower().strip()
if is_raining == "yes":
    if umbrella =="yes":
        print("Go outside")
    else:
        print("stay inside or take an umbrella")
else:
    print("Enjoy your day")



#SMART ATM 

balance = int(input("Enter your bank balance:"))
withdrawal = int(input("How much money do you want to withdraw:"))
if balance >= withdrawal:
    print("Transaction successful")
    print("Remaining balance is:" balance-withdrawal)
else:
    print("Insufficient balance")

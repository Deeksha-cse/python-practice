#FOR VS WHILE
#for                                                               while
#used when you know the number of repetitions             used when you don't know how many
#                                                                 times it will repeat
name = "Python"
for letter in name:
    print(letter)
#P
#y
#t
#h
#o
#n is the output


#NESTED LOOPS
#   a loop inside a other loop
for i in range(3):
    for j in range(2):
        print(i,j)

#imagine two clocks 
#outer loop = hours 
#inner loop = minutes

#for every hour, the minutes go through all their values
i = 0
j = 0
j = 1
print(0,0)
print(0,1)
#now the inner loop finishes
#outer loop continues
i = 1
#inner loop starts from the beginning
j = 0
j = 1
print(1,0)
print(1,1)
i = 2
j = 0
j = 1
print(2,0)
print(2,1)


#Real life example 

#Imagine you're organizing classrooms

#There are 3 classrooms
#each classroom has 2 benches 
#the classroom are the outer loop
#the benches are the inner loop
for row in range(3):
    for col in range(2):
        print("*")
#how many starts will it print?
#outer loop 3
#inner loop 2
#total 6 stars


#why are nested loops useful?
#it is used whenever you're working with combinations

#pattern printing
for row in range(3):
    for col in range(4):
        print("*", end="")
        print()
#new thing ends=""
#normally 
print("hello")
print("hi")
#output is hello 
#hi 
#print automatically ends with /n (newline)
#but 
print("*" , end="")
print("*", end="")
print("*")
#output is ***
#because 
#ends="" tells python "don't go to the next line after printing"

for row in range(2):
    for col in range(3):
        print("@" ,end="")
    print()
#predicting the output
#outer loop 
#row 0,1
#col 0,1,2
#   @@@
#   @@@

#practice q1
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()

#practice q2
for row in range(5):
    for col in range(row+1):
        print("*", end="")
    print()
#output is 
# *
# **
# ***
# ****
# *****
#reverse of this
 
 # practice q3
for row in range(5):
    for col in range(5 - row):
        print("*",end="")
    print()

#practice q4
for row in range(5):
    for col in range(row +1):
        print(row + 1 ,end="")
    print()
#predicting the output
#rows 5 
#col1 1
#col2 22
#col3 333
#col4 4444
#col5 55555


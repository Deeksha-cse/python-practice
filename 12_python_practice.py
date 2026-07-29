#BREAK - stop the loop immediately
#imagine you're searching for your notebook in a stack of books 
#as soon as you find it, you stop searching
#that is exactly what break does
for num in range(1,11):
    if num == 5:
        break 
    print(num)
#output is 
1
2
3
4

#CONTINUE - skips the current iteration
#imagine you're checking exam papers
#if one paper is blank, you skip it and check the next one 
#that is exactly what continue does
for num in range(1,5):
   if num == 3:
       continue
   print(num)
#output
1
2
4
#the number 3 is skipped but the loop keeps running


#PASS - does nothing 
for num in range(1,6):
    if num == 3:
        pass 
    print(num)

#ouput 
1
2
3
4
5
#nothing special happens, Pass doesn't stop or skip anything-it simply does nothing

#it's mainly useful when you're writing code step by step or creating a program before filling in the details

#suppose you're building a game,but haven't written the "game over" logic yet
score = 100
if score == 0:
    pass # I'll write the code later
print("game is running")

#practice q1
for num in range(1,11):
    if num == 7:
        break 
    print(num)

#practice q2
for num in range(1,11):
    if num == 5:
        continue
    print(num)

#practice q3
for num in range(1,21):
    if num == 17:
        break 
    if num % 2 == 0:
        continue
    print(num)

#practice q4
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#practice q5
name = "Deeksha"
for i in name:
    if i  == "e":
        continue
    print(i)

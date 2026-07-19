#string mastery

#1 .lower()
name = "DeeKsHa".lower()
print(name)
#output is deeksha 
#lower() changes all letters to lowercase

#2 .upper()
name = "DeeKsHa" .upper()
print(name)
#output is DEEKSHA
#upper() changes all letters to upper case

#3 .strip()
name = " deeksha " .strip()
print(name)
#output is deeksha
#strip() #removes the spaces from the both ends

#lstrip() #removes the space from the left end

#rstrip() #removes the space from the right end


#4 .capitalize()
name = "deeksha".capitalize()
print(name)
#output is Deeksha

#5 .title()
city = "new york".title()
print(city)
#output is New York

#6 .replace()
quote = "practice makes man perfect"
print(quote.replace("man" , "woman"))
#replaces one word or character with other
#output is practice make woman perfect

#7. find()
name = "Deeksha"
print(name.find("k"))
#output is 3
#python counts from 0
# D e e k s h a
# 0 1 2 3 4 5 6
print(name.find("z"))
#output is -1

#8. count 
name = "banana"
print(name.count("n"))
#output is 2 



#string indexing
#one of the most important topic of python
#a string is sequence of characters
# remember always starts counting from 0 ,not 1
#syntax
#string[]
word = "Python"
print(word[0])
#output is P 
print(word[2])
#output is t

#negative indexing
# P  y  t  h  o  n 
# 0  1   2  3   4  5
#-6 -5   -4  -3 -2 -1

name = "Python"
print(word[-1])
#output is n

#index error
name = "Deeksha"
#the valid indexes are from 0 to 6 and -7 to -1
#output is index error

#len()
#finding length of the word
name = "Deeksha"
print(len(name))
#output is 7
#length starts from 1 while index start from 0

#combing with lower() strip() 
city = "Delhi" .lower()
print(city[0])
#output is d


# string slicing
#string indexing will give only one character
name = "programming"
print(name[3])
#output g

#string slicing gives you multiple characters
#syntax 
#string[start:stop]

#golden rule 
#the start index is included 
#the stop index is excluded

name = "programming"
print(name[0:3])
#output is pro

#if start = stop 
print(name[2:2])
#output is nothing

#if start is bigger
print(name[5:2])
#output is empty

#omitting the start
print(name[:4])
#python assume start = 0
#output is prog

#omitting the stop 
print(name[3:])
#python assumes to go until the end
#output is gramming

#omitting both
print(name[:])
#python assumes to start from the beginning and go till the end
#output is programmming

#negative slicing
#p r o g r a m m i n g
#0 1 2 3 4 5 6 7 8 9 10
#-9 -8 -7 -6 -5 -4 -3 -2 -1

word = "programming"
print(word[-3:])
#output is ing

word = "Uma"
print(word[-3:-2])
#output U

word = "Python"
# p y t h o n
#-6-5-4-3-2-1
print(word[:-2])
#output python stops before-2
#output is pyth
#always takes from left to right

#step value
#step tell python to skip characters
#syntax 
#string[start:stop:step]

word = "Deeksha"
print(word[0:6:2])
#output is Des
# so basically 
#start with 0 (D)
#jump 2 letters (e)
#jump 2 letters (s)
#6 index is not included


#reverse string
#one of the coolest python features
word = "Python"
print(word[::-1])
#meaning 
# start from the beginning and go until the end
# here -1 indicate to move backward and jump 1 letter
# P y t h o n
# n o h t y p

#why does python start from the end
#this is the special rule you need to remember
print(word[::-1])
#you didn't tell python where to start
#since the step is negative where to start
#python automatically says ;
#oh! you're walking backwards. i'll start from back wards
#that's all
#it is a built in rule


#practice q1
username = input("enter your name:")
username ="deeksha"
print(username.uppercase())

#practice q2
college = input("enter your college name:").lower()
college = "MAHE"
print(college)

#practice q3
sentence = " jack of all master of none ".strip()
print(sentence)

word = "Deeksha"
print(word.replace("e","@"))

word = 'deeksha'
print(word.count("e"))

#practice q4
word = input("enter the name of the file")
if word[0:2] == "py":
    print("Good")
else:
    print("the file should start with py")

#practice q5
word = input("enter the name of the file")
if word[-3:] == ".py":
    print("done")


#practice q6
word = input("enter the name of file:")
if word.endswith(".py"):
    print("done")

#practice q7
word = input("enter your gmail address:")
if word.endswith("@gmail.com"):
    print("valid gmail")
else:
    print("not a gmail address")

#practice q8
name = input("enter your name").lower().strip()
print(name)

#practice q9
sentence = input("enter a sentence:").lower()
if "python" in sentence:
    print("python is present")
else:
    print("python is not required")

#the 'in' operator asks 
# 'is the word present anywhere inside the string'

word = input("enter your name:")
if ("a" in word or
    "e" in word or
    "i" in word or
    "o" in word or
    "u" in word):
    print("contains vowel")
 


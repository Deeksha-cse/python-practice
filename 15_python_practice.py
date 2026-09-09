#python lists
#a list lets you to store multiple items in a single variable 
#instead of 
student1 = "rahul"
student2 = "priya"
student3 = "rohit"
#you can store all the students in a list
students =[ "rahul","priya","rohit"]
print(students[0])
#rahul 
print(students)
#"rahul","priya","rohit"
students.append("deeksha")
print(students)
#includes deeksha in the list 
#loop through the list
students =["rahul","priya","rohit"]
for student in students:
    print(student)

#challenge 1 
subjects = ["fee","emsb","cm","pps","evs"]
for subject in subjects:
    print(subjects)
    print(subjects[0])
    print(subjects[0] and subjects[4])
    # or
    print(subjects[-1])
    #gives the last element of the list 


#challenge 2
subjects = ["fee","emsb","cm","pps","evs"]
subjects[2] = "maths"
print(subjects)
#changes cm to maths in the list
subjects.append("python")
subjects.remove("pps")
#removes pps from the list
#removes the value not the index
#remove(0) will not work because 0 is the index not the value
subjects.insert(1,"python")
#insert python at index 1 
#while append adds the value at the end of the list insert adds the value at a specific index
print(subjects)
print(len(subjects))
#prints the number of elements in the list 


marks = [90,80,70,60,50]
marks.sort()
print(marks)
#arranges the elements in ascending order
marks.sort(reverse=True)
print(marks)
#arranges the elements in descending order

#challenge 3
marks = [78,45,92,61,88]
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
print(marks.count(78))
#counts the number of times 78 is present in the list

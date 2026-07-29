#else with loops 

for i in range(4):
    print(i)
else:
    print("loop finished")

#if doesn't mean the same thing as if.. else
#for loop "else" means 
#run this code only if the loop finishes normally(without break)
#in the above example the loop finished normally without break so, loop finish is printed

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("done")

#here the output is 
0
1
2
#done is not printed 


for i in range(4):
    if i == 3:
        continue
    print(i)
else:
    print("finished")

#here finished is also printed



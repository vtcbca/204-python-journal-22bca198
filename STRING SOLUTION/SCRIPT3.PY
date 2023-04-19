def evenstr(y):
    z=[]
    count=0
    for i in y:
        if(len(i)%2==0):
            z.append(i)
            count=count+1
    if(count>0):
         print(f"the number of even string is {count} and string:{z}")

    else:
         print("no even string available!")
y=[]
for i in range(5):
     e=input(f"Enter string:{i+1}:")
     y.append(e)
evenstr(y)
 

def change(x):
    y=[]
    z=int(input("Enter value you want to replace:"))
    c=int(input("Enter value you want to change with:"))
    for i in x:
        if z==i:
            y.append(c)
        else:
            y.append(i)    
    print(y)

def createlist():
    a=[]
    b=int(input("How many numbers you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter a number:"))
        a.append(c)
    change(a)

createlist()

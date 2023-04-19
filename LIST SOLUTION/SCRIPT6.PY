def evenodd(a):
    even,odd=[],[]
    count1,count2=0,0
    for i in  a:
        if i%2==0:
            even.append(i)
            count1+=1
        else:
            odd.append(i)
            count2+=1

    print(f"the even number are {count1} and numbers:")
    printlist(even)
    print(f"the odd number are {count2} and numbers:")
    printlist(odd)

def printlist(b):
    for i in b:
        print(i)

def createlist():
    c=[]
    d=int(input("How many number you want to enter in list:"))
    for i in range(d):
        e=int(input("Enter a number:"))
        c.append(e)
    evenodd(c)


createlist()

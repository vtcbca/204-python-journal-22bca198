def makedict(a):
    dict1={}
    b=int(input("Enter minimum word length:"))
    for i in a:
        if len(i)>=b:
            dict1[i]=len(i)

    print(dict1)

def input1():
    str=input("Enter sentence:")
    a=str.split(" ")
    makedict(a)

input1()    

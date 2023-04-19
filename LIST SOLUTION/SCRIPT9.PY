def dict(n):
    dict1={}
    for i in range(0,len(n),3):
        dict1[n[i]]=n[i+1:i+3]

    print(dict1)
def input1():
    q=[]
    i="y"
    while i=="y" or i=="Y":
        z1=int(input("Student id:"))
        q.append(z1)
        z2=input("Student name:")
        q.append(z2)
        z3=float(input("Student percentage:"))
        q.append(z3)
        i=input("Do you add more ?(y/Y):")
    print(q)
    dicto(q)

input1()
   

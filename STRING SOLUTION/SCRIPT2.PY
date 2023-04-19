def paliwordcount(x):
    y=x.split(" ")
    z=0
    l=[]
    for i in y:
        if (i==i[::-1]):
            z=z+1
            l.append(i)
    if z>0:
        print(" Palindrome Word In Sentence Is {z} And Palindrome Words Are:{l}.")              
    else:
        print(" No Palindrome Word in Sentence!!!")    
x=input("enter a sentece:")
paliwordcount(x)

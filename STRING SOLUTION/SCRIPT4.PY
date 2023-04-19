a=[]
b="y"
while b=="y" or b=="Y":

    print("\n MENU")
    print("1.add items in a list.\n")
    print("2. Print string with even character in length. ")
    print("3.Replace odd character of string with index no.")
    print("4. Enter start and end value and extract character from the list of string.")
    print("5.exit")

    c=int(input("Enter a choice !"))

if c==1:
    b1="y"
    while b1=="y" or b1=="Y":
        d=input("Enter a string you want to enter :")
        a.append(d)
        a1=input("do you add more string press(y/Y):")
elif c==2:
    e=[]
    count=0
    for i in a:
        if(len(i)%2==0):
            e.append(i)
            count+=1
        if count>0:
            print(f"string with even character is {e}")
        else:
            print("string has no even character in it .")

elif c==3:
    f=[]
    for i in a:
        for j in range(0,len(i),2):
            i[j]=j
            f.append(i)
            print(f)

elif c==4:
    g=int(input("enter start index :"))
    h=int(input("enter end index:"))
    j=" ".join([sub for sub in a])[s:e]
    print(f"your string is{j}")

else:
    print("enter a valid choice !")

k=input("Do you want to continue:(y/Y):")

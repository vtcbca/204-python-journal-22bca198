def name(a):
    filechange=[]
    b=".c"
    for i in a:
        if b in i:
            c=i.replace(".c",".py")
            filechange.append(c)
        else:
            filechange.append(i)

print(filechange)


filename=["program.c","stdio.c","conio.c","math.py","a.py","b.py"]

name(filename)

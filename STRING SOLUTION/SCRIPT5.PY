def symmetric(w):
    x=(len(w)//2)
    y=w[:x]
    z=w[x:]
    if y==z:
        print(f"string {w} is symmetric !")
    else:
        print(f"string {w} is not symmetric")

def input1():
    e=input("Enter a string:")
    symmetric(e)

input1()

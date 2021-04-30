num1=eval(input("first number?"))
num2=eval(input("second number?"))
l1={}
l2={}
nat1=1
nat2=1
while input("check another thousand?")!="no":
    l1.clear()
    l2.clear()
    for x in range(nat1,nat1+1000):
        l1[x*num1]=x
    nat1=x
    for x in range(nat2,nat2+1000):
        l2[x*num2]=x
    nat2=x
    for x in l1.keys():
        for y in l2.keys():
            if y==x:
                print(f"the lcm is {y}, with times {l1[x]} for the first number and times {l2[y]} for the\nsecond number")


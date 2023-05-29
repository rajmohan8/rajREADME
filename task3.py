r= int(input("enter red"))
g= int(input("enter green"))
b= int(input("enter blue"))
if( r>=200 and g<=60 and b<=60):
    print("range of red")
elif(r<=160 and g>=200 and b<=102):
    print("range of green")
elif(r<=60 and g<=150 and b>=200):
    print("range of blue")
else:
    print("unknown")

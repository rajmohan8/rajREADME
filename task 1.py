'''
guess the number
'''
input("Enter the name of the player")
n=int(input("enter any number"))
x= 100
print("total point:100")
for i in range (n):
    p=int(input("p"))
    if p<n :
        x=x-5
        print(x)
        print("p is too low")
    if p>n:
        x=x-5
        print(x)
        print("p is too high")
    if p==n:
        
        print("p is correct")
        print("final x",x)
        
    


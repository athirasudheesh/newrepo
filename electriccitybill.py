n=int(input("enter the electricity unit"))
if n<=100:
    print("no charge")
elif(n<=200):
    print("your current bill is",n*5)
elif(n<=300):
    print("your curent bill is",n*10)
else:
    print("default")
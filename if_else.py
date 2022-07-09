name=input("enter your name")
age=int(input("enter your age"))
print(name,"...you are eligible for voting") if age>=18 else print(name,"...you are not eligible for votting")
print(f"your age is {age}")
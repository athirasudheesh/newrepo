a=[]
print("enter the numbers")
for i in range(8):
    i=int(input())
    a.append(i)
count_5=a.count(a[4])
if count_5==3:
    print("TRUE") 
else:
    print("FALSE")    

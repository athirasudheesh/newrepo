import re
def lovefind(name,count):
    x=re.findall("l",name)
    count=len(x)+count
    x=re.findall("o", name)
    count=len(x) + count
    x=re.findall("v", name)
    count=len(x)+count
    x=re.findall("e", name)
    count=len(x)+count
    return count
def truefind(name,count):
    x = re.findall("t", name)
    count = len(x) + count
    x = re.findall("r", name)
    count = len(x) + count
    x = re.findall("u", name)
    count = len(x) + count
    x = re.findall("e", name)
    count = len(x) + count
    return count

count1=0
count2=0
count3=0
count4=0
c=0
name1=input("enter the first name")
name2=input("enter the second name")
count1=truefind(name1,count1)
count2=truefind(name2,count1)
count3=lovefind(name1,count3)
count4=lovefind(name2,count3)
count2=str(count2)
count4=str(count4)
c=count2+count4
c=int(c)
if c<10 or c>90:
    print("Your score is **",c,"**, you go together like coke and mentos.")
elif 40<c<50:
    print("Your score is **",c,"y**, you are alright together.")
else:
    print("Your score is **",c,"**.")






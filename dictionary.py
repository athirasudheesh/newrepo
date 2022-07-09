a={"name":"athira","age":"23","place":"calicut"}
b={"name":"sreny","age":"21","location":"alapuzha"}
c={"name":"ammu","age":"26","location":"kottayam"}
keys=["name","age"]
for k in keys:
    print(a[k],end=" ")
c.pop("location")
print(c)
for k in keys:
    b.pop(k)
print(b)
for k in keys:
    print(a[k],end=",")
print()
for k in keys:
    print(c[k],end=",")

t1 = (1,2,3,5,6,1,4,2,3,1,3,3,2)
print(t1.count(1))
print(t1.index(3))
d1 = {"Prasad":"Pizza", "Rohan":"Chicken","Harsh":"Thepla", "Meet": "Frankie",
      "Yash":{"Breakfast":"Eggs", "Lunch":"Fish", "Dinner":"Lobster"}}
del d1["Meet"]
print(d1)
print(d1["Yash"])
print(d1["Yash"]["Breakfast"])
d3 = d1.copy()
del d3["Prasad"]
print(d1)
print(d1.get("Rohan"))
d1.update({"Leena":"Candy"})
print(d1)
print(d1.keys())
print(d1.items())
d1.pop("Leena")
print(d1)
d1.popitem()
print(d1)
a = d1.setdefault("Prasad", "Sandwiches")
print(a)





d2 = {"key1","key2","key3"}
d3 = "Prasad"
thisdict = dict.fromkeys(d2,d3)
print(thisdict)




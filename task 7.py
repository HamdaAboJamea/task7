#Q\1
names = ["Tarteel", "Asmaa", "Ahmed"]
names.insert(0, "Sabrin")
print(names)
names.pop()
print(names)
names.append("Hamda")
print(names)
names.remove("Asmaa")
print(names)

#Q\2
friends = ["Adel", "Ahmed"]
employees = ["Samah", "Amjad"]
school = ["Ali","Basma"]
friends.extend(employees)
friends.extend(school)
print(friends)


#Q\3
dic1 = {1 :10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

#Q\4
d = dict()
for i in range(1, 16):
    d[i] = i**2
print(d)


#Q\5
d1 = {"a": 100, "b": 200, "c": 300}
d2= {"a": 150, "b": 200, "d": 400}
d3 = {}

for i,j in d1.items():
    for x,y in d2.items():
        if i == x:
            d3[i] = (j + y)
        if i not in d2 :
            d3[i] = (j)
        if x not in d1 :
            d3[x] = (y)

print(d3)

#Q\6
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
dic = dict(zip(keys, values))
print(dic)


#Q\7
sampleDict = {
    "class": {
        "student":{
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class'] ['student'] ['marks'] ['history'])




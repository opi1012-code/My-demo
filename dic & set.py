#dictionary=unorered,mutable,dont allow duplicate
# info={
#     "key":"value",
#    "name" : "Rabeya",
#    "learning":"coding",
#    "sub":["C","python"],
#    "topics":("dic","set"),
#    "age":23,
#    "is adult":True,
#    "marks":90.5
# }
# print(info)
# print(info["age"])
# info["age"]=34
# print(info["age"])
# null_dict={}
# null_dict["name"]="MySchool"
# print(null_dict)
#nested dictionary
myDict={
    "Morning":"butter,banana",
    "Noon":{
        "Rice":3,
        "Curry":10
    }
}
# print(myDict)
# print(myDict["Noon"]["Curry"])
#methods
# print(myDict.keys())
# print(list(myDict.keys()))
# print(myDict.values())
# print(list(myDict.items()))/
# p=list(myDict.items())
# print(p[0])
# print(myDict.get("Morning"))/
# print(myDict[("Noon")])

# myDict.update({"Morning":"Apple"})
# print(myDict)/
n={"Morning":"Apple Juice"}
myDict.update(n)
print(myDict)
#set=unordered,unique,immutable

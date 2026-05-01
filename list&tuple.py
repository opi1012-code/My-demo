#list=mutable= cng kora jabe bt str cng kora jabe na.
#str=12,12,"rabeya" unmutable
age=[23,26,27,16,20]
print(age[1])
print(len(age))
student=["Rabeya Afrin.",23,"Dhaka."]
student[0]="Afia Jannat Noor."
print("My name is",student[0])
print("I am ",student[1],"years old.")
print("I am from",student[2])
#list slicing
age=[23,26,27,16,21]
age[0]=20
print(age[-4:-2])
#list methods
list=[6,2,3]
list.append(5)# add one element at the end

print(list)
list.sort()#re-arrange smaller to elder
print(list)
list.sort(reverse=True)#re-arrange elder to smaller
print(list)
list.reverse
print(list)
list.insert(2,80)#add an element
print(list)
list.remove(2)
print(list)
list.pop(1)
print(list)
#Tuples==immutable(like string)
tup=(3,5,7,3)
print(type(tup))
#method

print(tup.index(7))
print(tup.count(3))


 
grade=("c","d","a","a","b","b","a")
print(grade.count("a"))
#palindrome= soro theke porle ja hobe ses theke porele tai hobe
list1=[1,2,1]

copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")
    
  


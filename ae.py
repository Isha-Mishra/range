def positive(lists):
    for j in range(list1):
        if (lists[j]>=0):
            print(lists[j],end=' ')
lists = []
list1 = int(input("enter total numbers of list elements:"))
for i in range(1,list1 + 1):
    value = int(input("please enter value of %d element:"%i))
    lists.append(value)
print("\n positive numbers in this list are:")
positive(lists)

        
    


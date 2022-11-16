list1 = ["Naveen", "Hari", "Balaji", "Nirai", "Kali", "Jai"]
list2 = ["98", "98", "88", "99", "76", "69"]
result = list()

# getting odd Number from list1
result = list1[1::2]
print("Odd Number", result)

# getting even Number from list1
result = list2[0::2]
print("Even Number", result)

# Merging 2 element
merge = list()
merge.extend(list1)
merge.extend(list2)
result = merge
print("Merging lists", merge)

# removing particular element
result.remove("Balaji")
print(result)

# adding new element into the list
result.insert(2, "Balaji")
print(result)

# remove the entire list
#del result
#print(result)

# reverse list
result.reverse()
print(result)

# clear all the element from list
result.clear()
print(result)


# Concatenate two lists index-wise
list1 = ["Naveen", "Hari", "Balaji", "Nirai", "Kali", "Jai"]
list2 = ["98", "98", "88", "99", "76", "69"]
result = [i+j for i,j in zip(list1, list2)]
print(result)

# concatenate two lists in the following order
list1 = ["Naveen", "Hari", "Balaji", "Nirai", "Kali", "Jai"]
list2 = ["98", "98", "88", "99", "76", "69"]
result = [x+y for x in list1 for y in list2]
print(result)

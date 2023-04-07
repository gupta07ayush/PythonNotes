# Given a list in python and provided the positions of the elemenets,
# write a program to swap the two elements in the list.

# input: List = [1,2,3,4,5], pos1=2, pos2= 5
#output: [1,5,3,4,2]


def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
    print(list)


list = [1,2,3,4,5]
print(list)
pos1, pos2 = 1,3

print(swap(list, pos1-1, pos2-1))
print()



# Method 2  using pop

list = [1,2,3,4,5,6,7]
print(list)
pos2, pos5 = 2,5

second = list.pop(pos2-1)
print(second)
fifth = list.pop(pos5-2)
print(fifth)
print(list)

list.insert(pos2-1, fifth)
list.insert(pos5-1, second)
print(list)

print()
# method 3
myls = [1,2,3,4,5,6,7]
print(myls)
pos2,pos5 = 2,5

get = list[pos2], list[pos5]
myls[pos5], myls[pos2] = get

print(myls)
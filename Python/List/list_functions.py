# num_list = [1,2,3,4,5,6,7,8,9,10]

# num_list = num_list[::2]
# print(num_list)

# a =[1,2,3]
# a.append(4)
# print(a)

# a.extend([5,7,8,9,10])
# print(a)

# b= [1,2,3,4,5,7,8,9,10]
# b.insert(5,6)
# print(b)

# b.remove(7)
# print(b)

# Remove by index (by default last) pop(index)
# a =[1,5,8,9]
# a.pop(0) 
# print(a)

# a.pop()
# print(a)

# index() -- return position 
a =[10,20,30,40]
print(f"Position of 30 is {a.index(30)}")

b = [1,2,5,3,2,5,2,4,2,2]
b=b.count(2)
print(b)

lst = [5,4,3,6,2,1,7,9,8]  # un sorted list
lst.sort()
print(lst)   # sorted list

lst.reverse()
print(lst)

lst.clear()
print(lst)

lst2= [10,20,30,40]
print(lst2[1])

for i in lst2:
    print(i)
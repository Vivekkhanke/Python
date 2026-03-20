num_list = [1,2,3,4,5,6,7,8,9,10]
names = ["Vivek","Satyajeet","Sagar","Rutuj"]

print(names[2])
print(num_list)

# for i in num_list:
#     print(i*2)

names.append("Shubham")
print(names)

# list.insert(position, "Value")
# Add value at specific position
names.insert(1,"Ram")
print(names)

# remove() Remove a specific value
fruits = ["Apple","Banana","Mango"]
fruits.remove("Banana")
print(fruits)

# pop() Remove value by index
fruits = ["Apple","Banana","Mango"]
fruits.pop(2)
print(fruits)

shopping_cart = []
shopping_cart.append("Shirt")
shopping_cart.append("Shoes")
shopping_cart.append("Tshirts")
shopping_cart.append("Jeans")
print(shopping_cart)

# Iteration through Lists
fruits = ["Apple","Banana","Mango","kivi","Orange"]
for f in fruits:
    print(f)

# iteration through index

for f in range(len(fruits)):
    print(f)
    

# To-Do list -Used in task management apps
task= []
task.append("study")
task.append("gym")
task.append("office")
print(task)
print("---------------------------------------")


email = ["vivek@gmail.com","abc@gmail.com","ram@gmail.com"]

for e in email:
    # print("Sending email to : ",e)
    print("---------------------------------------")
    print(f"Sending email to {e} mail id...!!!")
    

f = ["vivek","Ram"]
print(f[1])
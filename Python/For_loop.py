# Loop
# Syntax
# for variable in sequence:
#     code
# -------------------------------------------
# Print numbers 1 to 5

for i in range(1,6):
    print(i)
    
names = ["Rutuj","Vivek", "Satyajeet", "sagar", "Tejas"]

for i in names:
    print(i)
for i in range(1,11):
    print(i)

for i in range(1,11):
    if i == 6:
        break
    print(i)

for i in range(1,11):
    if i == 6:
        continue
    print(i)
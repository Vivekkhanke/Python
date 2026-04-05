#  Read file # write mode "r"
file = open("F:\Python Programs\Python\File Handling\sales.csv", "r")
f = file.read()
print(f)
file.close()

file = open("F:\Python Programs\Python\File Handling\sales.csv", "r")
oneline = file.readline()
print(oneline)
file.close()

oneline = file.readlines()
print(oneline)
file.close()

with open("F:\Python Programs\Python\File Handling\sales.csv", "r") as file:
    content = file.read()
    print(content)
    
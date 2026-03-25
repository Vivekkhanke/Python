students = {
    "id" : 123,
    "name": "Vivek",
    "age" : 26,
    "course":"Python",
    "list" : [1,2,3,4,5],
    "tup" : (1,2,4,5,6),
    "set" : {1,4,7,8,5,2}
}

# print(students["name"])
# print(students["age"])
# print(students["set"])

s = {"name":"Vivek", "age" : 26}
print(s["name"])

# Add value in dict
s["grade"] = "A"
print(s)

# Update dict
s["age"] = 20
print(s)

# loop
for k, v in s.items():
    print(k,v)

# Nested dict
 = {
    "s1student": {"name":"Sgar", "age":20},
    "s2": {"name": "Rutuj", "age":20}
}

print(student["s1"])
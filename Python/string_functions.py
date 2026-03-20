#String methods and operations

text ="Python"

print(text.upper())
print(text.lower())

# strip() (Remove Spaces)
name = "  Ram  "
nm = name.strip()
print(nm)

# replace("old_str", "new_str")
p = "Hello World"
q=p.replace("World","Vivek")
print(q)
# ------------------------------

clg = "G H Raisoni colleges"
print(clg.find("H"))     # Find is use to fine the position of the character
print(clg.find("soni"))
print("------------------------------")


abc = "A,B,C,D,E,F"  #.csv
print(abc.split(","))

abc = "V | I | V | E | K"  #.csv
print(abc.split("|"))



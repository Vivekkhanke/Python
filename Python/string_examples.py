
text ="     Data Enginner       "
clean = text.strip().lower()

print(clean)
print("----------------------------------------")

email = input("Enter your email : ")  #vivek123@gmail.com  @, . ?

if "@" in email and "." in email:
    print("Your email is Valid")
else:
    print("Email is not valid")
 


# Extarct information from text

text ="OrderID:1234567"
print(text)

orderid = text.split(":")[0]
print(orderid)

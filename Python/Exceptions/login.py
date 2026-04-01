def login(age):
    try:
        age = int(age)
        if age < 18:
            return "Access Denied"
        else:
            return "Access Granted"
    except ValueError:
        return "Invalida input.. Age must be number"
    
# res = login("14")
# print(res)
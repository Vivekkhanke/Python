age = int(input("Enter your age : "))
citizion = input("Are you a citizion? (yes/no) : ")
city = input("Enter the city name : ")
# citizion =YES
if age>=18:
    if citizion.lower() == "yes":
        print("You r eligible to vote")
        if city =="pune":
            print("Your are eligible for vote in pune only")
        else:
            print("Your are not part of pune city")
    else:
        print("only citizion can vote")
else:
    print("You are not eligible due to age")      
    
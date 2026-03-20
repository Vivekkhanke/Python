# name = "Nayan"
# teacher ="Madam"
# lv = "Level"

pl = input("Enter the name : ").lower()
reverse = pl[::-1]

if pl == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
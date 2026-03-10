marks = int(input("Enter the marks : "))

if marks >= 90:
    grade ="A+"
    
elif marks >= 75:
    grade = "A"
    
elif marks >= 60:
    grade = "B"

elif marks >=50:
    grade ="C"

else:
    grade = "F"

print("Grade : ",grade)

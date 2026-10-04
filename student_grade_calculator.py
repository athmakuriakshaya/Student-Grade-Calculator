print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter your name: ")

mark1 = float(input("Enter Subject 1 marks: "))
mark2 = float(input("Enter Subject 2 marks: "))
mark3 = float(input("Enter Subject 3 marks: "))

total = mark1 + mark2 + mark3
percentage = total / 3

print("\n===== RESULT =====")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
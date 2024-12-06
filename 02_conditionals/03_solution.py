score = int(input("Provide me your number: "))

if score >= 90:
   print("Please verify your grade.")
   exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade: ", grade)
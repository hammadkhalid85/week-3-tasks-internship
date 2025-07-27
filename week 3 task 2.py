print("\n=== Task 2: Marks and Grades ===")
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = (total / 300) * 100  # assuming each subject is out of 100

if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Total: {total}, Percentage: {percentage:.2f}%, Grade: {grade}")

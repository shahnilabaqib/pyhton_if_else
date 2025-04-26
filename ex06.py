# 🔹Exercise 6: Scholarship Check
# Input:

# grade (A, B, C, etc.)

# sports_participation (yes/no)

# If:

# Grade is A or B and

# participated in sports → Eligible for scholars

grade = input("Enter your Grade: ")

sports_participation = input("Have you participated in sports: (yes/no)").strip().lower()

if grade == "A" or "B" and sports_participation == "yes":
        print("Eligible for scholrship")


else:
        print("You are not Eligible")




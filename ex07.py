# 🔹Exercise 7: Driver's License Eligibility
# Ask:

# age

# vision_test_passed (yes/no)

# Eligible if:

# age >= 18 and

# passed vision test


age = int(input("Enter your age:"))
vision_test_passed = input("Have you passsed vission test? (yes/no)").strip().lower()

if age >= 18 and vision_test_passed == "yes":
    print("You are eligible for driving license")

else:
    print("You are not elegible")

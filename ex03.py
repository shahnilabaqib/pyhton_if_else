# Exercise 3: Discount Eligibility
# Ask user:

# age

# is_student (yes/no)

# If the person is either:

# a student or

# under 18
# They get a discount.

age = int(input("Enter Your Age:"))
is_studen = input(("Are You A Student:" "Yes/no"))
student = is_studen.lower() == "yes"

if ( age <= 18 and student ):
        print("Get your Discount") 
else:
        print("You Are Not Elegeble To Get Discount")



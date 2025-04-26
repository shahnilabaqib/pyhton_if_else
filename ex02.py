# 🔹Exercise 2: Student Exam Result
# Take input for:

# score (0–100)

# attendance (percentage)

# Pass if:

# score is 60 or more and

# attendance is 80% or more

score = int(input("Enter Your Score: (0-100)"))
attendance = int(input("Enter your Attendence: "))

if ( score >= 60 and attendance >= 80 ):
    print ("Pass")

else:
    print("Fail")

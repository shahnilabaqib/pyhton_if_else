# 🔹Exercise 4: Job Application Check
# Ask for:

# education_level (bachelor/master)

# years_experience

# Select candidate if:

# Education is "master" and experience >= 2
# OR

# Education is "bachelor" and experience >= 4

education_level = input(" Enter your education Bachelor / Master")
years_experience = int(input("Enter Years: "))
education = education_level.strip().lower()



if ( education and years_experience > 2 ):
 
     print("Congratulations: You Are Selected")

else:
     print("you are not selected")



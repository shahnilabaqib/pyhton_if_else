# 🔹Exercise 1: Park Entry
# Ask the user for their age and membership status.
# Allow entry if:

# Age is between 18 and 60 and

# The person is a member (yes).

age = int(input("Enter Your Age: "))
membership_status = input("Are You a Member? (Yes/No)")

membership = membership_status.lower() == "yes"

if (age > 18 and age < 60 and membership):
       print("You Are Allowed")

elif (age < 18 or age > 60 ):
     print("You Are Not Allowed")

else:
      print ("Plz Register to Enter")

         
        
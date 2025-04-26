# 🔹Exercise 8: Movie Ticket Offer
# Ask:

# day (Friday, Saturday, etc.)

# is_student (yes/no)

# If:

# It’s Friday or Saturday and student → Ticket is half price

day = input("Book your day:(Friday, Saturday, etc.)").strip().lower()
is_student = input("Are you a student (yes/ no)").strip().lower()

if day == "friday" and "saturday" and is_student == "yes":
        print("Ticket is half price")

else:
        print("Ticket is full price")
                


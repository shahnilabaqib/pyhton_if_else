# 🔹Exercise 5: Online Purchase Eligibility
# Ask:

# has_account (yes/no)

# cart_total (amount)

# Allow purchase if:

# account is created and

# cart_total is more than 500

has_account = input(" Do you have an account (yes/no)").strip().lower()
cart_total = int(input("Enter your total cart amount:"))

if has_account == "yes" and cart_total >= 500:
        print("You can proceed")

elif has_account == "no":
        print("Create acount first")

elif has_account == "yes" and cart_total < 500:
        print("Please purchase above 500 to proceed")

else:
       print("please createe acount and shop above 500")


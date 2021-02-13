from data_manager import DataManager

data_manager = DataManager()


print(f"""
Welcome to Beth's Flight Club. 
Sign up here for email notifications.
""")

continue_verification = True
first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()
user_email = input("What is your email?\n")
while continue_verification:
    email_confirmation = input("Type your email again, please.\n")
    if email_confirmation == user_email:
        print("Alright! You're in the club.")
        data_manager.add_customer(
            first_name,
            last_name,
            user_email)
        continue_verification = False
    else:
        print("Emails don't match.")
        continue
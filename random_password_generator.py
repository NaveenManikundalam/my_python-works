import string, random

while True:
    opinion = input("Do you want to generate a password ? Please reply with (Yes/No) = ")
    opinion = opinion.lower()
    char = list(string.ascii_letters + string.digits + "!@#$%^&*")

    def generate_passowrd():
        password = []
        random.shuffle(char)
        for i in range(pass_len):
            password.append(random.choice(char))
        password = "".join(password)
        return password

    if opinion == "yes":
        print("Great. Let's generate a password for you")
        while True:
            try:
                pass_len = int(input("Enter the length of your password = "))
                break
            except ValueError:
                print("Encountered a Value error. Please enter an integer value")
        print(f"Your password for this transaction will be = {generate_passowrd()}")
        break
    elif opinion == "no":
        print("Thank you for your time. Have a nice day")
        break
    else: 
        print('Invalid input. Please reply with a "Yes" or a "No"')

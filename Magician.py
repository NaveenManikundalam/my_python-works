secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

entry= int(input('Enter the number = '))

while entry != 777:
    print("Ha ha! You're stuck in my loop!")
    entry= int(input('Enter the number = '))

else:
    print("Well done, muggle! You are free now")
    

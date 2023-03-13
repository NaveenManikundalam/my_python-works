import random

def guess(min, max):
    comp_guess = random.randint(min, max)
    user = input(f"Is {comp_guess} is the number that you have in our mind??. Please say Yes(Y) or No(N) = ").lower()
    while True:
     if user == "y": 
          print("Told you I am a smart computer.")
          break
     else:
        user = input(f"Is the {comp_guess} more(M) or less(L) than the number ?? ").lower()
        if user == "m":
          max = comp_guess-1
          comp_guess = random.randint(min, max)
          user = input(f"Is {comp_guess} is the number that you have in our mind??. Please say Yes(Y) or No(N) = ").lower()
        else:
          min = comp_guess+1
          comp_guess = random.randint(max, max)
          user = input(f"Is {comp_guess} is the number that you have in our mind??. Please say Yes(Y) or No(N) = ").lower()

guess(1,100)


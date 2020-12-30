print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case=name1 + name2
combined_case=lower_case.lower()

t=combined_case.count("t")
r=combined_case.count("r")
u=combined_case.count("u")
e=combined_case.count("e")

true=t+r+u+e

l=combined_case.count("l")
o=combined_case.count("o")
v=combined_case.count("v")
e=combined_case.count("e")

love=l+o+v+e
score=int(str(true) + str(love))

if (score<10) or (score>90):
  print(f"Your love score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your love score is {score}, you are alright together.")

else:
  print(f"your love score is: {score}")
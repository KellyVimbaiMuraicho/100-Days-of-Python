steps = int(input("How many steps did you walk this week? "))
required_steps = 2500

if steps >= required_steps:
    print("Congratulations, you have qualified for a reward!")
else:
    print("You have not reached the required weekly streak.")
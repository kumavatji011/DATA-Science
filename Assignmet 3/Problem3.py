import random

balls = ['R'] * 5 + ['G'] * 7 + ['B'] * 8
trials = 1000

prev_blue = 0
prev_blue_and_red = 0
total_red = 0
total_blue = 0
blue_after_red = 0

previous = random.choice(balls)

for i in range(trials):
    current = random.choice(balls)

    if previous == 'B':
        prev_blue += 1
        if current == 'R':
            prev_blue_and_red += 1

    if previous == 'R' and current == 'B':
        blue_after_red += 1

    if current == 'R':
        total_red += 1
    if current == 'B':
        total_blue += 1

    previous = current

# Conditional probability from simulation
p_red_given_blue = prev_blue_and_red / prev_blue

# Bayes theorem calculation using simulation values
p_blue_given_red = blue_after_red / total_red
p_red = total_red / trials
p_blue = total_blue / trials

bayes_result = (p_blue_given_red * p_red) / p_blue

# Results
print("P(Red | Blue) from simulation:", p_red_given_blue)
print("P(Red | Blue) using Bayes theorem:", bayes_result)

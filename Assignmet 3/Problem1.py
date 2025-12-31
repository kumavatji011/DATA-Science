import random

# Total number of trials
trials = 10000

# ------------------------------
# (a) Coin Toss Simulation
# ------------------------------
heads = 0
tails = 0

for i in range(trials):
    toss = random.choice(['H', 'T'])
    if toss == 'H':
        heads += 1
    else:
        tails += 1

prob_heads = heads / trials
prob_tails = tails / trials

# ------------------------------
# (b) Two Dice Simulation
# ------------------------------
sum_7_count = 0

for i in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        sum_7_count += 1

prob_sum_7 = sum_7_count / trials

# ------------------------------
# Results
# ------------------------------
print("Coin Toss Simulation:")
print("Heads:", heads, "Probability:", prob_heads)
print("Tails:", tails, "Probability:", prob_tails)

print("\nTwo Dice Simulation:")
print("Sum = 7 count:", sum_7_count)
print("Probability of getting sum 7:", prob_sum_7)

import random

def probability_at_least_one_six(trials=10000):
    success = 0

    for i in range(trials):
        got_six = False
        
        for j in range(10):
            if random.randint(1, 6) == 6:
                got_six = True
                break
        
        if got_six:
            success += 1

    return success / trials

# Calling the function
prob = probability_at_least_one_six()
print("Probability of getting at least one 6 in 10 rolls:", prob)

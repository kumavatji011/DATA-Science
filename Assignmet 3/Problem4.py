import numpy as np

# Sample size
n = 1000

# Possible values and their probabilities
values = [1, 2, 3]
probabilities = [0.25, 0.35, 0.40]

# Generate sample
sample = np.random.choice(values, size=n, p=probabilities)

# Calculate statistics
mean = np.mean(sample)
variance = np.var(sample)
std_deviation = np.std(sample)

# Output results
print("Empirical Mean:", mean)
print("Empirical Variance:", variance)
print("Empirical Standard Deviation:", std_deviation)

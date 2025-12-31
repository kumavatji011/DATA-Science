import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate uniform random numbers
population = np.random.uniform(low=0, high=1, size=10000)

# Step 2: Draw samples and calculate means
sample_size = 30
num_samples = 1000
sample_means = []

for i in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))

# Step 3: Visualization
plt.figure(figsize=(12, 5))

# Uniform distribution
plt.subplot(1, 2, 1)
plt.hist(population, bins=30, density=True)
plt.title("Uniform Distribution")
plt.xlabel("Value")
plt.ylabel("Density")

# Sample mean distribution
plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=30, density=True)
plt.title("Distribution of Sample Means (n = 30)")
plt.xlabel("Sample Mean")
plt.ylabel("Density")

plt.tight_layout()
plt.show()

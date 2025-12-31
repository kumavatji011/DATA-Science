import numpy as np
import matplotlib.pyplot as plt

# Parameters
mean = 5
samples = 2000

# Generate exponential random samples
data = np.random.exponential(scale=mean, size=samples)

# Create histogram
plt.hist(data, bins=30, density=True, alpha=0.6, label='Histogram')

# Generate values for PDF
x = np.linspace(0, max(data), 1000)
pdf = (1 / mean) * np.exp(-x / mean)

# Plot PDF
plt.plot(x, pdf, 'r', label='PDF')

# Labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Exponential Distribution (Mean = 5)')
plt.legend()

# Show plot
plt.show()

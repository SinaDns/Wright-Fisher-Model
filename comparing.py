import numpy as np
import matplotlib.pyplot as plt


def wright_fisher_simulation(population_size, initial_frequency, num_generations):
    allele_freq = [initial_frequency]

    for generation in range(1, num_generations):
        sampled_alleles = np.random.binomial(population_size, allele_freq[-1]) / population_size
        allele_freq.append(sampled_alleles)

    return allele_freq


def plot_simulation(allele_freq, label):
    generations = range(len(allele_freq))
    plt.plot(generations, allele_freq, label=label)


plt.figure(figsize=(10, 6))

# Simulation 1: N = 100, p = 0.7
population_size_1 = 100
initial_frequency_1 = 0.7
num_generations = 100

allele_freq_1 = wright_fisher_simulation(population_size_1, initial_frequency_1, num_generations)
plot_simulation(allele_freq_1, 'N=100, p=0.7')

# Simulation 2: N = 10000, p = 0.3
population_size_2 = 10000
initial_frequency_2 = 0.3

allele_freq_2 = wright_fisher_simulation(population_size_2, initial_frequency_2, num_generations)
plot_simulation(allele_freq_2, 'N=10000, p=0.3')

plt.xlabel('Generations')
plt.ylabel('Allele Frequency')
plt.title('Wright-Fisher Model Simulation')
plt.legend()
plt.grid(True)
plt.show()

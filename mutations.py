import numpy as np
import matplotlib.pyplot as plt


def wright_fisher_simulation(population_size, initial_frequency, mutation_rate, num_generations):
    allele_freq = [initial_frequency]

    for generation in range(1, num_generations):
        sampled_alleles = np.random.binomial(population_size, allele_freq[-1]) / population_size
        mutated_alleles = np.random.binomial(population_size, mutation_rate)
        allele_freq.append((sampled_alleles + mutated_alleles) / (population_size + mutation_rate))

    return allele_freq


plt.figure(figsize=(10, 6))

# Parameters for simulation 1
population_size_1 = 100
initial_frequency_1 = 0.7
mutation_rate_1 = 0.4
num_simulations_1 = 5

# Parameters for simulation 2
population_size_2 = 10000
initial_frequency_2 = 0.3
mutation_rate_2 = 0.1
num_simulations_2 = 5

## We can add more simulations. after finding another parameters, we must add another "for _" loop to show that in plot.


# results for simulation 1
for _ in range(num_simulations_1):
    allele_freq_1 = wright_fisher_simulation(population_size_1, initial_frequency_1, mutation_rate_1, 100)
    plt.plot(range(len(allele_freq_1)), allele_freq_1, color='red', alpha=0.5)

# results for simulation 2
for _ in range(num_simulations_2):
    allele_freq_2 = wright_fisher_simulation(population_size_2, initial_frequency_2, mutation_rate_2, 100)
    plt.plot(range(len(allele_freq_2)), allele_freq_2, color='blue', alpha=0.5)

## results for other simulations can be added  here

plt.xlabel('Generations')
plt.ylabel('Allele Frequency')
plt.title('Wright-Fisher Model Simulations with Mutation')
plt.grid(True)
plt.show()

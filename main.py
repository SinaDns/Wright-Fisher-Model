import numpy as np
import matplotlib.pyplot as plt


def wright_fisher_simulation(population_size, initial_frequency, num_generations):
    allele_freq = [initial_frequency]

    for generation in range(1, num_generations):
        sampled_alleles = np.random.binomial(population_size, allele_freq[-1]) / population_size
        allele_freq.append(sampled_alleles)

    return allele_freq


plt.figure(figsize=(10, 6))

# Parameters for simulation 1
population_size_1 = 100
initial_frequency_1 = 0.7
num_simulations_1 = 10

# Parameters for simulation 2
population_size_2 = 10000
initial_frequency_2 = 0.3
num_simulations_2 = 10

# # We can add more parameters for simulation 3,4,... like we added below:
# population_size_3 = 3
# initial_frequency_3 = 0.5
# num_simulations_3 = 5

# results for simulation 1
for _ in range(num_simulations_1):
    allele_freq_1 = wright_fisher_simulation(population_size_1, initial_frequency_1, 100)
    plt.plot(range(len(allele_freq_1)), allele_freq_1, color='red', alpha=0.5)

# results for simulation 2
for _ in range(num_simulations_2):
    allele_freq_2 = wright_fisher_simulation(population_size_2, initial_frequency_2, 100)
    plt.plot(range(len(allele_freq_2)), allele_freq_2, color='blue', alpha=0.5)

# results for simulation 3,4,... as we said above (uncomment and run for better define)
# for _ in range(num_simulations_3):
#     allele_freq_3 = wright_fisher_simulation(population_size_3, initial_frequency_3, 100)
#     plt.plot(range(len(allele_freq_3)), allele_freq_3, color='black', alpha=0.5)

print(np.__version__)
plt.xlabel('Generations')
plt.ylabel('Allele Frequency')
plt.title('Wright-Fisher Model Simulations')
# plt.legend()
plt.grid(True)
plt.show()
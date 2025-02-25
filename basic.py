import numpy as np
import matplotlib.pyplot as plt


def wright_fisher_simulation(population_size, initial_frequency, num_generations):
    allele_freq = [initial_frequency]

    # Simulation loop
    for generation in range(1, num_generations):
        sampled_alleles = np.random.choice([0, 1], size=population_size, p=[1 - allele_freq[-1], allele_freq[-1]])
        new_frequency = np.mean(sampled_alleles)
        allele_freq.append(new_frequency)

    return allele_freq


def plot_simulation(allele_freq):
    generations = range(len(allele_freq))

    plt.plot(generations, allele_freq, marker='o', linestyle='-')
    plt.xlabel('Generations')
    plt.ylabel('Allele Frequency')
    plt.title('Wright-Fisher Model Simulation')
    plt.grid(True)
    plt.show()


population_size = 100
initial_frequency = 0.5
num_generations = 50

allele_freq = wright_fisher_simulation(population_size, initial_frequency, num_generations)

plot_simulation(allele_freq)
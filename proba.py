import random

def simulate_genders(num_simulations):
    at_least_one_girl = 0
    all_girls = 0

    for i in range(num_simulations):
        girls = 0
        for j in range(3):
            if random.random() < 0.5:
                girls += 1
        if girls >= 1:
            at_least_one_girl += 1
            if girls == 3:
                all_girls += 1

    return all_girls / at_least_one_girl

num_simulations = 1000
probability = simulate_genders(num_simulations)
print("Probability of all children being girls given at least one girl: {:.3f}".format(probability))
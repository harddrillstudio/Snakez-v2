from Individual import Individual
import random


class Population:
    pop_size = 20
    individuals = []
    gvars = None

    def __init__(self, gvars, l=None):
        if l is not None:
            self.individuals = l
        else:
            self.gvars = gvars
            for i in range(self.pop_size):
                self.individuals.append(Individual(gvars))

    def get_best_fitness(self):
        return min(indiv.get_fitness() for indiv in self.individuals)

    def compute_fitness(self):
        for indiv in self.individuals:
            indiv.get_fitness()

    def tournament_select(self):
        players = random.sample(self.individuals, 10)
        return min(players, key=lambda indiv: indiv.get_fitness())

    def crossover(self, mother, father):
        offspring = Individual(self.gvars)

        for i in range(offspring.segment_quantity):
            average_gene = (mother.genes[i] + father.genes[i]) / 2
            offspring.genes[i] = average_gene
        offspring.get_fitness()
        return offspring

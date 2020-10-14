import random
import numpy as np

from individual import Individual

class Population:
    def __init__(self, population=100, target=None):

        self.pop = [Individual(target=target) for i in range(population)]
        self.s = int(len(self.pop) / 2)  # half of len pop
        self.target = target
        self.target_pop = population

    def next_gen(self):
        """calc all fitnesses
        based on fitness select 2 parents

        mutation step > override self.pop met nieuwe kinders"""
        # self.evolve() # make children
        scores = []
        for i in self.pop:
            i.random_mutate()  # randomly suffer from mutation
            scores.append(i.fitness(self.target))
        # get best 2 performers
        index_best_pop = sorted(range(len(scores)), key=lambda sub: scores[sub])[-2:]
        self.pop = [self.pop[i] for i in index_best_pop]
        self.s = int(len(self.pop) / 2)  # half of len pop
        self.evolve()

    def evolve(self):
        """evolve"""
        f, m = self._prep_orgie()
        children = self._mate(f, m)
        self.pop.extend(children)

    def _prep_orgie(self):
        """Everyone preps to mate
        random shuffle the index of the pop, split that in half,
        assign one half as fathers and the other as mothers.
        """

        shuffld_pop = self.pop
        np.random.shuffle(shuffld_pop)
        fathers = shuffld_pop[: self.s]
        mothers = shuffld_pop[self.s :]
        return fathers, mothers

    def _mate(self, fathers, mothers):
        new_children = self.target_pop - len(self.pop)
        children = [Individual(target=self.target) for i in range(new_children)]
        len_parent = len(fathers)
        # print("len parents = ", len_parent)
        for i in range(new_children):
            rand_int = random.choice(range(len_parent))
            # print("rand int = ", rand_int)
            dna_index_shuffle = np.arange(0, len(self.target))
            np.random.shuffle(dna_index_shuffle)
            father_dna_index = dna_index_shuffle[: self.s]
            # print("dna index = " , father_dna_index)
            mother_dna_index = dna_index_shuffle[self.s :]
            dna_father = fathers[rand_int - 1].provide_dna(father_dna_index)
            dna_mother = mothers[rand_int - 1].provide_dna(mother_dna_index)
            children[i].dna_inject(
                dna_father, father_dna_index, dna_mother, mother_dna_index
            )

        return children

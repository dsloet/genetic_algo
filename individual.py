import random
import string
import numpy as np

class Individual:
    def __init__(self, mutate_prob=1, target=None):
        self.dna = list(
            "".join(random.choice(string.ascii_lowercase) for i in range(len(target)))
        )
        self.mutate_prob = mutate_prob

    def random_mutate(self):
        """random mutation of the self.dna"""
        i = random.uniform(0, 1)
        if i < self.mutate_prob:
            # random pick a letter and mutate
            x = np.random.choice(range(len(self.dna)))  # get random index
            self.dna[x] = random.choice(string.ascii_lowercase)

    def dna_inject(self, dna_father, father_dna_index, dna_mother, mother_dna_index):
        """inject dna after mating"""
        combined_dna = dna_father + dna_mother  # combine the dna
        combined_index = np.append(
            father_dna_index, mother_dna_index
        )  # combine the index
        self.dna = [
            combined_dna[i] for i in combined_index
        ]  # get the new dna in correct order

    def provide_dna(self, index_list):
        return [self.dna[i] for i in index_list]

    def fitness(self, target):
        """How fit am I?"""
        target = list(target)
        counter = 0

        for i in range(len(self.dna)):
            if self.dna[i] == target[i]:
                counter += 1
        self.score = counter / len(target)
        if self.score == 1.0:
            print("DONE!")
        return counter / len(target)

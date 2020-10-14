from population import Population

target = "mothers"
group = Population(target=target)

max_score_ever = []
max_score_ever.append(0)
for i in range(5000):
    group.next_gen()
    score = []
    for j in group.pop:
        score.append(j.fitness(target))
        max_score_ever.append(max(score))

    if i % 200 == 0:
        print(max(max_score_ever), i)
    # if (i % 500 == 0):
    #   print(group.pop[0].dna)
    if max(score) == 1.0:
        print("DONE, ", score, i)
        break
    # for i in group.pop:
    #   print(i.dna)

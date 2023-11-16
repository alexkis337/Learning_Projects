import random

import matplotlib.pyplot as plt
from more_itertools import random_permutation


class Dove:
    counter = 0
    def __init__(self, pile = None):
        self.name = f'Dove_{self.counter}'
        Dove.counter += 1
        self.strategy = 'dove'
        self.score = 0
        self.pile = pile

class Hawk:
    counter = 0
    def __init__(self):
        self.name = f'Hawk_{self.counter}'
        Hawk.counter += 1
        self.strategy = 'hawk'
        self.score = 0


class Environment:
    def __init__(self, agents, food_amount=50):
        self.agents = agents
        self.food_amount = food_amount

    # here we randomly select two agents and make them play the game, d/d = 1/1, h/h = 0.5/0.5, d/h = 0/2
    @staticmethod
    def play(agent_1=None, agent_2=None):
        if agent_1 is None and agent_2 is None:
            pass
        elif agent_1 is None:
                agent_2.score += 2
        else:
            if agent_2 is None:
                agent_1.score += 2
            else:
                if agent_1.strategy == 'dove' and agent_1.strategy == agent_2.strategy:
                    agent_1.score += 1
                    agent_2.score += 1
                elif agent_1.strategy == 'hawk' and agent_1.strategy == agent_2.strategy:
                    agent_1.score += 0.5
                    agent_2.score += 0.5
                else:
                    if agent_1.strategy == 'dove':
                        agent_1.score += 0
                        agent_2.score += 2
                    else:
                        agent_1.score += 2
                        agent_2.score += 0
    # for i in range(self.food):
    #     play()

#
# for i in range(50):
#     print(random.choice(['dove', 'hawk']))

doves = [Dove(), Dove()]
orig_doves = doves
hawks = [Hawk(), Hawk()]
orig_hawks = hawks

env = Environment([doves[0], doves[1], hawks[0], hawks[1]])

start, end = 0, env.food_amount
non_repeating_numbers_list = list(random_permutation(range(start, end))*2)
random.shuffle(non_repeating_numbers_list)

process_piles = list()

for dove in doves:
    dove.pile = non_repeating_numbers_list[0]
    process_piles.append(non_repeating_numbers_list[0])
    non_repeating_numbers_list.pop(0)

for hawk in hawks:
    hawk.pile = non_repeating_numbers_list[0]
    process_piles.append(non_repeating_numbers_list[0])
    non_repeating_numbers_list.pop(0)

process_piles = list(set(process_piles))

# print(f'Processing {process_piles}')
# print('----------------------------')

for pile in sorted(process_piles):
    print(f'Pile is {pile}')

    try:
        instance1 = list(filter(lambda x: x.pile == pile, doves))
        agent1 = doves[int(instance1[0].name.split('_')[1])]
    except:
        try:
            instance1 = list(filter(lambda x: x.pile == pile, hawks))
            agent1 = hawks[int(instance1[0].name.split('_')[1])]
        except:
            agent1 = None
    agent1.pile = None
    # print(f'agent1 is {agent1}')

    try:
        instance2 = list(filter(lambda x: x.pile == pile, doves))
        agent2 = doves[int(instance2[0].name.split('_')[1])]
    except:
        try:
            instance2 = list(filter(lambda x: x.pile == pile, hawks))
            agent2 = hawks[int(instance2[0].name.split('_')[1])]
        except:
            agent2 = None
    # print(f'agent2 is {agent2}')

    env.play(agent1, agent2)

    for dove in doves:
        if dove.score == 0:
            doves.remove(dove)
        elif dove.score == 0.5:
            if random.randint(0,1) == 0:
                doves.remove(dove)
            else:
                pass
        elif dove.score == 1:
            pass
        elif dove.score == 1.5:
            if random.randint(0,1) == 0:
                pass
            else:
                doves.append(Dove())
        else:
            doves.append(Dove())

    for hawk in hawks:
        if hawk.score == 0:
            hawks.remove(hawk)
        elif hawk.score == 0.5:
            if random.randint(0,1) == 0:
                hawks.remove(hawk)
            else:
                pass
        elif hawk.score == 1:
            pass
        elif hawk.score == 1.5:
            if random.randint(0,1) == 0:
                pass
            else:
                hawks.append(Hawk())
        else:
            hawks.append(Hawk())

# plotting stacked chart

    # print(f'Processing {process_piles}')
    # print('----------------------------')

    # print(f'{doves[0].name} = {doves[0].score}, '
    #       f'{doves[1].name} = {doves[1].score}, '
    #       f'{doves[2].name} = {doves[2].score}, '
    #       f'{doves[3].name} = {doves[3].score}, '
    #
    #       f'{hawks[0].name} = {hawks[0].score}, '
    #       f'{hawks[1].name} = {hawks[1].score},'
    #       f'{hawks[2].name} = {hawks[2].score}')

# name = list(instance)[0].name
    # print(f'dove {name}')



    # get_bird = name.split('_')[1]
    # print(get_bird)



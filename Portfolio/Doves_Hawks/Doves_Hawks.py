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
    def __init__(self, pile = None):
        self.name = f'Hawk_{self.counter}'
        Hawk.counter += 1
        self.strategy = 'hawk'
        self.score = 0
        self.pile = pile

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
                    agent_1.score += hawk_hawk_score
                    agent_2.score += hawk_hawk_score
                else:
                    if agent_1.strategy == 'dove':
                        agent_1.score += dove_hawk_score
                        agent_2.score += 2 - dove_hawk_score
                    else:
                        agent_1.score += 2 - dove_hawk_score
                        agent_2.score += dove_hawk_score


doves = [Dove(), Dove()]
hawks = [Hawk(), Hawk()]
result = []
input_iterations = int(input('How many iterations?\n'))

hawk_hawk_score = float(input('Hawk/Hawk score?\n'))
dove_hawk_score = float(input('Dove/Hawk score?\n'))

############## iteration starts here #####################

for i in range(input_iterations):
    print('\n------------------------------------------------------------------------------------')
    print(f'Iteration {i}')
    env = Environment(doves + hawks)

    for bird in env.agents:
        bird.score = 0

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
    print(process_piles)
    # print(f'Processing {process_piles}')
    # print('----------------------------')

    print(f'ITERATION START: {len(doves)} doves | {len(hawks)} hawks')
    for pile in sorted(process_piles):
        try:
            instance1 = list(filter(lambda x: x.pile == pile, doves))
            agent1 = doves[hawks.index(instance1[0])]
        except:
            try:
                instance1 = list(filter(lambda x: x.pile == pile, hawks))
                agent1 = hawks[hawks.index(instance1[0])]
            except:
                agent1 = None
        try:
            agent1.pile = None
        except:
            pass

        try:
            instance2 = list(filter(lambda x: x.pile == pile, doves))
            agent2 = doves[doves.index(instance2[0])]
        except:
            try:
                instance2 = list(filter(lambda x: x.pile == pile, hawks))
                agent2 = hawks[hawks.index(instance2[0])]
            except:
                agent2 = None
        try:
            agent2.pile = None
        except:
            pass
        # print(f'agent2 is {agent2}')
        env.play(agent1, agent2)


    new_doves = doves.copy()
    new_hawks = hawks.copy()

    for dove in doves:
        if dove.score == 0:
            new_doves.remove(dove)
        elif 0 < dove.score < 1:
            if random.random() > dove.score:
                new_doves.remove(dove)
            else:
                pass
        elif dove.score == 1:
            pass
        elif 1 < dove.score < 2:
            if random.random() + 1 > dove.score:
                pass
            else:
                new_doves.append(Dove())
        else:
            new_doves.append(Dove())
    for hawk in hawks:
        if hawk.score == 0:
            new_hawks.remove(hawk)
        elif 0 < hawk.score < 1:
            if random.random() > hawk.score:
                new_hawks.remove(hawk)
            else:
                pass
        elif hawk.score == 1:
            pass
        elif 1 < hawk.score < 2:
            if random.random() + 1 > hawk.score:
                pass
            else:
                new_hawks.append(Hawk())
        else:
            new_hawks.append(Hawk())

        doves = new_doves
        hawks = new_hawks

    print(f'ITERATION END: {len(doves)} doves | {len(hawks)} hawks\n')
    result.append({'iteration': i, 'doves': len(doves), 'hawks': len(hawks)})
    doves = new_doves
    hawks = new_hawks

print(result)
# Extracting result
iterations = [entry['iteration'] for entry in result]
dove_counts = [entry['doves'] for entry in result]
hawk_counts = [entry['hawks'] for entry in result]

# Calculate total counts
total_counts = [d + h for d, h in zip(dove_counts, hawk_counts)]

# Stackplot
plt.stackplot(iterations, dove_counts, hawk_counts, labels=['Doves', 'Hawks'], colors=['blue', 'red'])

# Add labels and title
plt.xlabel('Iterations')
plt.ylabel('Species Counts')
plt.legend(loc='upper left')
plt.title(f'Doves and Hawks Population Over Iterations\n Hawk-Hawk Score = {hawk_hawk_score} | '
          f'Dove-Hawk Score = {dove_hawk_score}')

# Display the legend

# Show the plot
plt.show()
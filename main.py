import random
import matplotlib.pyplot as plt

dove_counter = 0
hawk_counter = 0
num_doves = [] # list to store dove counts over time
num_hawks = [] # list to store hawk counts over time

def dove_simulation(doves: dict):
    ### NOTE: There are only 100 sources of food, with 2 morsels at each location ###
    global dove_counter # use the global dove_counter variable
    baby_doves = []
    dead_doves = []
    # dove goes to a resource
    for dove in doves:
        source_loc = random.randint(0, 99)
        doves[dove]['source'] = source_loc

    # check how many doves are at which location
    access_count = [0] * 100
    for dove in doves:
        source_loc = doves[dove]['source']
        access_count[source_loc] += 1
    
    # calculate how much food each dove gets
    for dove in doves:
        source_loc = doves[dove]['source']
        amt_food = 2 / access_count[source_loc]
        doves[dove]['amount-food'] = amt_food
        doves[dove]['score'] += amt_food

        # dove dies if less than one morsel of food
        if doves[dove]['amount-food'] < 1:
            dead_doves.append(dove)

        # dove reproduces if 2 morsels of food
        if doves[dove]['amount-food'] == 2:
            dove_counter += 1
            baby_doves.append(f'dove_{dove_counter}')
    
    for dead_dove in dead_doves:
        del doves[dead_dove]

    for baby_dove in baby_doves:
        doves[baby_dove] = {
            'source': 0,
            'amount-food': 0,
            'score': 0
        }
    
    num_doves.append(len(doves))
    
def dove_and_halk(doves: dict, hawks:dict):
    global dove_counter
    global hawk_counter
    baby_doves = []
    baby_hawks = []
    dead_doves = []
    dead_hawks = []

    # dove goes for a resource
    for dove in doves:
        source_loc = random.randint(0, 99)
        doves[dove]['source'] = source_loc

    # hawk goes for a resource
    for hawk in hawks:
        source_loc = random.randint(0,99)
        hawks[hawk]['source'] = source_loc

    # check how many doves and hawks are at each location
    # first element is dove, and second is hawk
    access_count = [[0,0] for _ in range(100)]
    for dove in doves:
        source_loc = doves[dove]['source']
        access_count[source_loc][0] += 1
    for hawk in hawks:
        source_loc = hawks[hawk]['source']
        access_count[source_loc][1] += 1

    for dove in doves:
        source_loc = doves[dove]['source']
        if access_count[source_loc][1] == 0:
            amt_food = 2 / access_count[source_loc][0]
            doves[dove]['amount-food'] = amt_food
            doves[dove]['score'] += amt_food
            
            # dove dies if less than one morsel of food
            if doves[dove]['amount-food'] < 1:
                dead_doves.append(dove)

            # dove reproduces if 2 morsels of food
            if doves[dove]['amount-food'] == 2:
                dove_counter += 1
                baby_doves.append(f'dove_{dove_counter}')

        if (access_count[source_loc][1] == 1):
            if (access_count[source_loc][0] == 1):
                amt_food = .5
                doves[dove]['amount-food'] = amt_food
                doves[dove]['score'] += amt_food

                # simulate 50% chance of survival
                dove_death = random.random()
                if dove_death < 0.5:
                    dead_doves.append(dove)
            else: # if more than one dove and one hawk
                dead_doves.append(dove)

        # if more than 1 hawk, assume total carnation, blood, and death
        if (access_count[source_loc][1] > 1):
            dead_doves.append(dove)

    for hawk in hawks:
        source_loc = hawks[hawk]['source']
        if access_count[source_loc][1] == 1:
            if access_count[source_loc][0] == 0:
                amt_food = 2
                hawks[hawk]['amount-food'] = amt_food
                hawks[hawk]['score'] += amt_food

                hawk_counter += 1
                baby_hawks.append(f'hawk_{hawk_counter}')

            else: # if any doves are found at the scene
                amt_food = 1.5
                hawks[hawk]['amount-food'] = amt_food
                hawks[hawk]['score'] += amt_food

                # simulates 50% chance of reproduction
                hawk_repro = random.random()
                if hawk_repro < 0.5:
                    hawk_counter += 1
                    baby_hawks.append(f'hawk_{hawk_counter}')
        else: # if more than one hawk
            dead_hawks.append(hawk)

    unique_dead_doves = list(set(dead_doves))
    unique_dead_hawks = list(set(dead_hawks))

    for dead_dove in unique_dead_doves:
        del doves[dead_dove]

    for dead_hawk in unique_dead_hawks:
        del hawks[dead_hawk]

    for baby_dove in baby_doves:
        doves[baby_dove] = {
            'source': 0,
            'amount-food': 0,
            'score': 0
        }

    for baby_hawk in baby_hawks:
        hawks[baby_hawk] = {
            'source': 0,
            'amount-food': 0,
            'score': 0
        }

    num_doves.append(len(doves))
    num_hawks.append(len(hawks))
    
def main():
    global dove_counter
    global hawk_counter
    global num_doves
    global num_hawks
    doves = {
        'dove_0': {
            'source': 0,
            'amount-food': 0,
            'score': 0
        }
    }
    hawks = {
        'hawk_0': {
            'source': 0,
            'amount-food': 0,
            'score': 0
        }
    }
    # 1 year simulation
    for i in range(365):
        dove_simulation(doves)

    plt.plot(range(365), num_doves)
    plt.xlabel('Days')
    plt.ylabel('Number of Doves')
    plt.title('Dove Population Over Time')
    plt.grid(True)
    plt.show()

    # RESET GLOBALS #
    dove_counter = 0
    hawk_counter = 0
    num_doves = []
    num_hawks = []

    # RESET DOVES #
    doves = {
        'dove_0': {
            'source': 0,
            'amount-food': 0,
            'score': 0
        }
    }
    # 1 year simulation
    for i in range(365):
        dove_and_halk(doves, hawks)

    plt.plot(range(365), num_doves)
    plt.plot(range(365), num_hawks)
    plt.xlabel('Days')
    plt.ylabel('Number of Doves and Hawks')
    plt.title('Dove and Hawk Population Over Time')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
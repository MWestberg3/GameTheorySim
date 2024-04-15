import random
import matplotlib.pyplot as plt

dove_counter = 0
num_doves = [] # list to store dove counts over time

def dove_simulation(doves: dict):
    ### NOTE: There are only 1000 sources of food, with 2 morsels at each location ###
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
            continue

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
    
def main():
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

if __name__ == "__main__":
    main()
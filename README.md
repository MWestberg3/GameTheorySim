# Optional HW: Game Theory Simulation #
## Set up ##
After watching [this video](https://www.youtube.com/watch?v=YNMkADpvO4w), the following questions came up:
1. What happens when 3+ birds show up at a resource?
2. What if one hawk and 2+ doves?
3. What happens if 2+ hawks and 1+ dove?

These are my conclusions corresponding to the above questions, as answers were not found in resources available:
1. When 3+ birds show up at a resource, each bird divies up the resources such that if 3 birds arrive at a resource, each bird would get 2/3 of the resource.
2. The hawk gets the same amount, and the doves split the remainder.
3. All die.
## Results ##
### Part 1 ###
#### Dove Simulation ####
I find here that the population of doves levels out to approximately 120 doves when given only 100 locations for food over the course of one year. There are fluctuations of course, but they stay relatively close to 120 total doves.
#### Dove and Hawk ####
I find here the rough equilibrium. They both eventually level out together, though there tends to be more hawks than doves; however, they population of both added together is about the same as the Dove Only Simulation.

### Part 2 ###
#### Setup ####
I see here that my edge cases were answered here. At least mostly. I will set this up similar to how the Dove and Hawk Sim was set up. This also assumes that all of the rules above hold true. For example, if 1 hawk and 1 dove, the dove gets 1/2 morsels, while the hawk gets 3/2 morsels.
#### Results ####
Based on my algorith, I show very similar trends to what was shown in Part 1. There is some deviation, however the overall number of birds seems to remain the same.
### Comments ###
Based on the graphic results, I would say the equilibrium is much the same. It doesn't change all that much. However, I do notice that the amount of Doves increases with their probability of survival pending a collision to be 2 / n. I would say that the equilibrium shifts slightly to the left, allowing for more doves to survive. The number of hawks, however, doesn't appear to change much based on if they win or lose.
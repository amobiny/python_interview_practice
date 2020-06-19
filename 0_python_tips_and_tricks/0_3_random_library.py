
###########################################################################
# Random library
###########################################################################
import random
random.seed(221)                                # initialize the random number generator
a = random.random()                             # random float in [0, 1]
b = random.randint(a=2, b=6)                    # random integer in [a, b]; including a and b
f = random.uniform(a=2, b=18)                   # generates random "real" number in range [a, b)
g = random.normalvariate(mu=0, sigma=4)         # generate randomly from the normal N(m, s)
c = random.choice([2, 3, 4])                    # randomly picks from the list
d = random.randrange(start=1, stop=5, step=1)   # randomly selects from the range

sample_list = [1, 2, 3, 4, 5, 6]
random.shuffle(sample_list)                     # randomly shuffles "in place"

e = random.sample(sample_list, k=4)             # samples k values from the list (without replacement)

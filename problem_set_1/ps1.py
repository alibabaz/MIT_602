###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    start = time.time()
    final, temp, heavy, Theavy, cowz = [], [], 0, 0, cows.copy()
    Tcowz = cowz.copy()
    while len(cowz) > 0:
        while len(Tcowz) > 0:
            top = max(Tcowz, key=Tcowz.get)
            Theavy = heavy + cowz[top]
            if Theavy > limit:
                del Tcowz[top]
            else:
                del Tcowz[top]
                del cowz[top]
                temp.append(top)
                heavy = Theavy
        Tcowz = cowz.copy()
        final.append(temp)
        temp, heavy, Theavy = [] , 0, 0
    end = time.time()
    return final
    print(end - start)
#^213 steps for print('Cow Train:', greedy_cow_transport({'Dottie':
#85, 'Abby': 38, 'Daisy': 50, 'Buttercup': 72, 'Lilly': 24, 'Betsy': 65
#, 'Willow': 35, 'Coco': 10, 'Rose': 50, 'Patches': 12}, 100))
#ATTEMPT 2(BOTH WORK):

    final = []
    names = sorted(cows, key=cows.get, reverse=True)
    weight = sorted(cows.values(), reverse= True)
    cowz = {name: weight for name, weight in zip(names, weight)}
    while sum(cowz.values()) > 0:
        temp, heavy = [], 0
        for i in names:
            if heavy + cowz[i] <= limit:
                heavy += cowz[i]
                temp.append(i)
                cowz[i] = 0
        final.append(temp)
        for i in temp:
            names.remove(i) 
        
    return final
#^158 steps for print('Cow Train:', greedy_cow_transport({'Dottie':
#85, 'Abby': 38, 'Daisy': 50, 'Buttercup': 72, 'Lilly': 24, 'Betsy': 65
#, 'Willow': 35, 'Coco': 10, 'Rose': 50, 'Patches': 12}, 100))
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    bestlength, besttrain = (len(cows)+1), []
    for train in get_partitions(cows):
        x, Tweight = 0, []
        while x < (len(train)):
            for car in train:
                x += 1
                heavy = 0
                for cow in car:
                    heavy += cows[cow]
                Tweight.append(heavy)
            if max(Tweight) > limit:
                break
            trainlength = len(train)
            if trainlength < bestlength:
                bestlength = trainlength
                besttrain = train
    return besttrain
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    def timeBrute(cows, limit):
	start = time.time()
	brute_force_cow_transport(cows, limit)
	end = time.time()
	print(end - start)
    def timerGreedy(cows, limit):
	start = time.time()
	greedy_cow_transport(cows, limit)
	end = time.time()
	print(end - start)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))



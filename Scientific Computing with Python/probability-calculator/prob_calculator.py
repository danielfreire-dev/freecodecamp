import copy
import random
from collections import Counter

class Hat:

    def __init__(self, **kwargs):
        self.contents = []

        for k in kwargs.keys():
            for v in range(0,kwargs.get(k)):
                self.contents.append(str(k))

    def draw(self,amount):
        pulled_balls = []
        if amount > len(self.contents):
            #print("The number of balls to draw exceeds the available quantity, returning all the balls")
            return self.contents           
        else:
            for i in range(0,amount):
                contentslength = len(self.contents)
                randomnumber = random.randint(0,contentslength -1) #-1 to prevent out of range
                pulled_balls.append(self.contents[randomnumber])
                self.contents.remove(self.contents[randomnumber])
                
                
        return pulled_balls
            

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):

    M = 0 #how many times we get expected
    N = 0 #amount of experiments performed
    experiments = num_experiments
    
    for e in range(experiments):

        hatcopy = copy.deepcopy(hat)
        taken_balls = hatcopy.draw(num_balls_drawn)
        extracted = Counter(taken_balls) #convert to dict format
        contains_all = True

        #if Extracted contains Expected, M += 1
        for k,v in expected_balls.items():
            if k not in extracted.keys() or extracted.get(k) < expected_balls.get(k):
                contains_all = False
                break
                
        if contains_all == True:
                M += 1
            
        N += 1
                    

    probability = M/N
    print("Probability: ",probability)
    return probability
    


hat1 = Hat(blue=3,red=2,green=6)
experiment(hat=hat1, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)


hat2 = Hat(yellow=5,red=1,green=3,blue=9,test=1)
experiment(hat=hat2, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)

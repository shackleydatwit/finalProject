1. two heuristics:
Heuristic Function 1: For this function I summed up the distances between the sampleLocations. This is admissible since it will never 
overestimate the work needed to be done to collect all the samples. The distance between all the samples will always be lower than the 
starting locations going to collect all the samples. 
Heuristic Function 2: For this function I found the lowest distance from the current location to a sampleLocation. This function is 
admissible because the lowest distance between the current location and a sample is always going to be less than the total distance 
from the current location to collecting all of the samples. Both of my heuristic functions take advantage of the “weakened” parameters 
because they don’t really take block location into account; they just sum up distances. 

2. coding choices:
I am a bit new to Python, I’ve only done a few assignments in it in previous years so I’m sure my code isn't the cleanest or most 
efficient way to do some of this assignment but I thought it was interesting that I broke it all into different files. Originally when 
I started this assignment I had everything in SampleWorld but then I decided to organize it by the different search methods. So learning 
how to use the imports to different files was new to me. 

3. admissible algorithms:
My astar functions are all admissible as well as uniformCostSearch and iterativeDepthSearch. Since the uniformCostSearch is because 
we’re always taking things off the front of the openList that have the lowest cost to reach out of the states we know about. 
IterativeDepthSearch is admissible because it is very programmatic about how it searches. It uses the depthFirstSearch and in a loop 
starts at 1 to see if the goal state was at a depth of 1. And so on, we’re not going to come up with longer than optimal solutions 
because you would have already found it previously. My depthFirstSearch is not admissible because it is not an optimal search. It does 
not keep track of cost so therefore it could take extra steps to get to the sampleLocation.

4. assignment suggestions:
I dont really have any clear cut suggestions I thought the assignment was pretty clear in the directions provided. I reached out and asked
about the heuristic functions so I guess you could add a note theres no right way to do those as long as they're admissable. Maybe some 
skeleton code would have helped out too, I know some of the students in the program arent from cs background so some simple skeleton
code could have saved everyone some time on simple things. 

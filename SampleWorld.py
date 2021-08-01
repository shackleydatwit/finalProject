#!usrbinpython
import sys
#importing my functions from other files to run from this main file
from dfs_ids import *
from ucs import *
from aStar import *

file = None 
columns = None
rows = None
robotLocation = None
sampleLocations = []
blockedLocations = []
children = []

def main():   
    arguments = sys.argv
    if len(arguments) == 3:
        alg = str(arguments[1])
        heuristic = str(arguments[2])
    elif len(arguments) == 4:
        alg = str(arguments[1])
        heuristic = str(arguments[2])
        weight = int(arguments[3])
    else:
        if len(arguments) == 1:
            print('Please input an algorthm to implement with the sample world')
            sys.exit()
        else:
            alg = str(arguments[1])

    global file
    file = sys.stdin.readlines()
    global columns 
    columns = int(file.pop(0))
    global rows
    rows = int(file.pop(0))
    counter = 0

    for string in file:
        global sampleLocations, blockedLocations, robotLocation
        bLocations = []
        sLocations = []
        columnCount = 0
        for letter in string:
            if letter == "#":
                bLocations.append(columnCount)
            if letter == "*":
                sLocations.append(columnCount)
            columnCount += 1     
        if '@' in string:
            robotLocation = [counter, string.find('@')]
        counter += 1
        blockedLocations.append(bLocations)
        sampleLocations.append(sLocations)

    if alg == "dfs":
        depthFirstSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, children)
        return 0;
    elif alg == "ids":
        iterativeDeepeningSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, children)
        return 0
    elif alg == "ucs":
        uniformCostSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, children)
        return 0
    elif alg == "astar":
        aStarSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, heuristic, None)
        return 0
    elif alg == "astarWeight":
        aStarWeightSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, heuristic, weight)
    elif alg == "greedy":
        greedySearch(robotLocation, sampleLocations, blockedLocations, columns, rows, heuristic, None)
    return 0
main()
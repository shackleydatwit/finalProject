#!/usr/bin/python
import sys
import heapq
import time

generated = 0
expanded = 0
openLists = []
hashList = []

def aStarSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, herustic, weight):
    tic = time.perf_counter()
    global openLists, hashList, generated, expanded
    pathcost = 0
    totalCost = herusticValue(sampleLocations, herustic, robotLocation, weight) + pathcost
    heapq.heappush(openLists, (totalCost, robotLocation, sampleLocations))
    notFoundAll = True
    while notFoundAll:
        nodePos  = heapq.heappop(openLists)
        node = nodePos[1]
        sampleLocation = nodePos[2]
        hashTemp = hash(str(node)) + hash(str(sampleLocation))
        #We are checking if the location is already in the hashlist, if it is we continue on, skipping it
        if not hashTemp in hashList:
            hashList.append(hashTemp)
            expanded += 1
            if node[1] in sampleLocation[node[0]]:
                sampleLocation[node[0]].remove(node[1])
                print('S')
            if any(sampleLocation):
                pathcost = (nodePos[0] - herusticValue(sampleLocation, herustic, node, weight)) + 1
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0], node[1]-1], weight)
                    if not (totalValue, [node[0], node[1]-1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]-1], sampleLocation))
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0], node[1]+1], weight)
                    if not (totalValue, [node[0], node[1]+1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]+1], sampleLocation))
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0]-1, node[1]], weight)
                    if not (totalValue, [node[0]-1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]-1, node[1]], sampleLocation))
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0]+1, node[1]], weight)
                    if not (totalValue, [node[0]+1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]+1, node[1]], sampleLocation))
                        generated += 1
                        print('D')
            else:
                notFoundAll = False
    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')

def aStarWeightSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, herustic, weight):
    tic = time.perf_counter()
    global openLists, hashList, generated, expanded
    pathcost = 0
    totalCost = herusticValue(sampleLocations, herustic, robotLocation, weight) + pathcost
    heapq.heappush(openLists, (totalCost, robotLocation, sampleLocations))
    notFoundAll = True
    while notFoundAll:
        nodePos  = heapq.heappop(openLists)
        node = nodePos[1]
        sampleLocation = nodePos[2]
        hashTemp = hash(str(node)) + hash(str(sampleLocation))
        #We are checking if the location is already in the hashlist, if it is we continue on, skipping it
        if not hashTemp in hashList:
            hashList.append(hashTemp)
            expanded += 1
            if node[1] in sampleLocation[node[0]]:
                sampleLocation[node[0]].remove(node[1])
                print('S')
            if any(sampleLocation):
                pathcost = (nodePos[0] - herusticValue(sampleLocation, herustic, node, weight)) + 1
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0], node[1]-1], weight)
                    if not (totalValue, [node[0], node[1]-1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]-1], sampleLocation))
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0], node[1]+1], weight)
                    if not (totalValue, [node[0], node[1]+1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]+1], sampleLocation))
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0]-1, node[1]], weight)
                    if not (totalValue, [node[0]-1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]-1, node[1]], sampleLocation))
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    totalValue = pathcost + herusticValue(sampleLocation, herustic, [node[0]+1, node[1]], weight)
                    if not (totalValue, [node[0]+1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]+1, node[1]], sampleLocation))
                        generated += 1
                        print('D')
            else:
                notFoundAll = False
    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')

def greedySearch(robotLocation, sampleLocations, blockedLocations, columns, rows, herustic, weight):
    tic = time.perf_counter()
    global openLists, hashList, generated, expanded
    totalCost = herusticValue(sampleLocations, herustic, robotLocation, weight)
    heapq.heappush(openLists, (totalCost, robotLocation, sampleLocations))
    notFoundAll = True
    while notFoundAll:
        nodePos  = heapq.heappop(openLists)
        node = nodePos[1]
        sampleLocation = nodePos[2]
        hashTemp = hash(str(node)) + hash(str(sampleLocation))
        #We are checking if the location is already in the hashlist, if it is we continue on, skipping it
        if not hashTemp in hashList:
            hashList.append(hashTemp)
            expanded += 1
            if node[1] in sampleLocation[node[0]]:
                sampleLocation[node[0]].remove(node[1])
                print('S')
            if any(sampleLocation):
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    totalValue = herusticValue(sampleLocation, herustic, [node[0], node[1]-1], weight)
                    if not (totalValue, [node[0], node[1]-1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]-1], sampleLocation))
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    totalValue = herusticValue(sampleLocation, herustic, [node[0], node[1]+1], weight)
                    if not (totalValue, [node[0], node[1]+1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]+1], sampleLocation))
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    totalValue = herusticValue(sampleLocation, herustic, [node[0]-1, node[1]], weight)
                    if not (totalValue, [node[0]-1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]-1, node[1]], sampleLocation))
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    totalValue = herusticValue(sampleLocation, herustic, [node[0]+1, node[1]], weight)
                    if not (totalValue, [node[0]+1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]+1, node[1]], sampleLocation))
                        generated += 1
                        print('D')
            else:
                notFoundAll = False
    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')

#Heuristic Values calcuated with given input from the user when aStar method is selected
def herusticValue(sampleLocations, herustic, node, weight):
    distanceFromSample = []
    if weight is None:
        weight = 1
    #Heurisitic function 0: returns 0
    if herustic == 'h0':
        return 0
    #Heurisitic function 1: summed up the distances between the sampleLocations
    elif herustic == 'h1':
        tempList=[]
        for i in range(0, len(sampleLocations)):
            for sampleLocation in sampleLocations[i]:
                hValue = int(abs(node[0] - i) + abs(node[1] - sampleLocation))
                heapq.heappush(distanceFromSample, hValue)
        return weight * int(sum(distanceFromSample)/len(distanceFromSample))
    # Heurisitic function 2: returns the lowest distance from the current location to a sample
    elif herustic == 'h2':
        for i in range(0, len(sampleLocations)):
            for sampleLocation in sampleLocations[i]:
                hValue = int(abs(node[0] - i) + abs(node[1] - sampleLocation))
                heapq.heappush(distanceFromSample, hValue)
        return weight * heapq.heappop(distanceFromSample)
    else:
        return -1
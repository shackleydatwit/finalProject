#!/usr/bin/python
import sys
import heapq

generated = 0
expanded = 0
openLists = []
hashList = []

def aStarSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, herustic):
    global openLists, hashList, generated, expanded
    pathcost = 0
    totalCost = herusticValue(sampleLocations, herustic, robotLocation) + pathcost
    heapq.heappush(openLists, (totalCost, robotLocation))
    notFoundAll = True
    while notFoundAll:
        nodePos  = heapq.heappop(openLists)
        node = nodePos[1]
        hashTemp = hash(str(node)) + hash(str(sampleLocations))
        #We are checking if the location is already in the hashlist, if it is we continue on, skipping it
        if not hashTemp in hashList:
            hashList.append(hashTemp)
            expanded += 1
            if node[1] in sampleLocations[node[0]]:
                sampleLocations[node[0]].remove(node[1])
                print('S')
            if any(sampleLocations):
                pathcost = (nodePos[0] - herusticValue(sampleLocations, herustic, node)) + 1
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    totalValue = pathcost + herusticValue(sampleLocations, herustic, [node[0], node[1]-1])
                    if not (totalValue, [node[0], node[1]-1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]-1]))
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    totalValue = pathcost + herusticValue(sampleLocations, herustic, [node[0], node[1]+1])
                    if not (totalValue, [node[0], node[1]+1]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0], node[1]+1]))
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    totalValue = pathcost + herusticValue(sampleLocations, herustic, [node[0]-1, node[1]])
                    if not (totalValue, [node[0]-1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]-1, node[1]]))
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    totalValue = pathcost + herusticValue(sampleLocations, herustic, [node[0]+1, node[1]])
                    if not (totalValue, [node[0]+1, node[1]]) in openLists:
                        heapq.heappush(openLists, (totalValue, [node[0]+1, node[1]]))
                        generated += 1
                        print('D')
            else:
                notFoundAll = False
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')

#Heuristic Values calcuated with given input from the user when aStar method is selected
def herusticValue(sampleLocations, herustic, node):
    distanceFromSample = []
    #Heurisitic function 0: returns 0
    if herustic == 'h0':
        return 0
    #Heurisitic function 1: summed up the distances between the sampleLocations
    elif herustic == 'h1':
        tempList=[]
        for i in range(0, len(sampleLocations)):
            tempList = sum(sampleLocations[i])/len(sampleLocations[i])
            tempList.append(i,tempList)
        return sum(tempList)/len(tempList)
    # Heurisitic function 2: returns the lowest distance from the current location to a sample
    elif herustic == 'h2':
        for i in range(0, len(sampleLocations)):
            for sampleLocation in sampleLocations[i]:
                hValue = int(abs(node[0] - i) + abs(node[1] - sampleLocation))
                heapq.heappush(distanceFromSample, hValue)
        return heapq.heappop(distanceFromSample)
    else:
        return -1
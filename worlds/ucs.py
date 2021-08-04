#!/usr/bin/python
import sys
import heapq
import time

generated = 0
expanded = 0
openLists = []
hashList = [] 

#For this search method you mentioned in the assignment that 'open lists are held in heaps for fast insertion' so I used a heap here vs a list
def uniformCostSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, children): 
    tic = time.perf_counter()
    global openLists, hashList, generated, expanded
    pathcost = 0
    heapq.heappush(openLists, (pathcost, robotLocation))
    notFoundAll = True
    
    while notFoundAll:
        nodePos  = heapq.heappop(openLists)
        node = nodePos[1]
        hashTemp = hash(str(node)) + hash(str(sampleLocations))
        if not hashTemp in hashList:
            hashList.append(hashTemp)
            expanded += 1
            if node[1] in sampleLocations[node[0]]:
                sampleLocations[node[0]].remove(node[1])
                print('S')
            if any(sampleLocations):
                pathcost = nodePos[0] + 1
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    if not (pathcost, [node[0], node[1]-1]) in openLists:
                        heapq.heappush(openLists, (pathcost, [node[0], node[1]-1]))
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    if not (pathcost, [node[0], node[1]+1]) in openLists:
                        heapq.heappush(openLists, (pathcost, [node[0], node[1]+1]))
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    if not (pathcost, [node[0]-1, node[1]]) in openLists:
                        heapq.heappush(openLists, (pathcost, [node[0]-1, node[1]]))
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    if not (pathcost, [node[0]+1, node[1]]) in openLists:
                        heapq.heappush(openLists, (pathcost, [node[0]+1, node[1]]))
                        generated += 1
                        print('D')
            else:
                notFoundAll = False
    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')
    return 0;
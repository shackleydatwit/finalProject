#!/usr/bin/python
import sys
import time

generated = 0
expanded = 0
openLists = []
hashList = []

def depthFirstSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, children): 
    tic = time.perf_counter()
    global openLists, hashList, generated, expanded
    openLists.append(robotLocation)
    notFoundAll = True
    while notFoundAll:
        if len(openLists) == 0:
            return -1;
        
        node = openLists.pop(0)
        expanded += 1
        hashTemp = hash(str(node)) + hash(str(sampleLocations))
        if not hashTemp in hashList:
            hashList.append(hashTemp) 
            if node[1] in sampleLocations[node[0]]:
                sampleLocations[node[0]].remove(node[1])
                print('S')
            if any(sampleLocations):
                children = []
                temp = []
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    if not[node[0], node[1]-1] in openLists:
                        children.insert(0, [node[0], node[1]-1])
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    if not[node[0], node[1]+1] in openLists:
                        children.insert(0, [node[0], node[1]+1])
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    if not[node[0]-1, node[1]] in openLists:
                        children.insert(0, [node[0]-1, node[1]])
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    if not[node[0]+1, node[1]] in openLists:
                        children.insert(0, [node[0]+1, node[1]])
                        generated += 1
                        print('D')
                temp = children + openLists
                openLists=temp
            else:
                notFoundAll = False
    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')
    return 0


def iterativeDeepeningSearch(robotLocation, sampleLocations, blockedLocations, columns, rows, children): 
    tic = time.perf_counter()
    global openLists, hashList, generated, expanded
    openLists.append(robotLocation)
    notFoundAll = True
    levelDepth = 1
    depthList = []
    while levelDepth < float('inf'):
        node = openLists.pop(0)
        hashTemp = hash(str(node)) + hash(str(sampleLocations))
        #We are checking if the location is already in the hashlist, if it is we continue on, skipping it
        if not hashTemp in hashList:
            hashList.append(hashTemp) 
            expanded += 1
            if node[1] in sampleLocations[node[0]]:
                sampleLocations[node[0]].remove(node[1])
                print('S')
            if any(sampleLocations):
                children = []
                temp = []
                #L
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    if not[node[0], node[1]-1] in openLists:
                        children.insert(0, [node[0], node[1]-1])
                        generated += 1
                        print('L')
                #R
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    if not[node[0], node[1]+1] in openLists:
                        children.insert(0, [node[0], node[1]+1])
                        generated += 1
                        print('R')
                #U
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    if not[node[0]-1, node[1]] in openLists:
                        children.insert(0, [node[0]-1, node[1]])
                        generated += 1
                        print('U')
                #D
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    if not[node[0]+1, node[1]] in openLists:
                        children.insert(0, [node[0]+1, node[1]])
                        generated += 1
                        print('D')
                depthList.extend(children)
                if len(openLists) == 0:
                    openLists = depthList
                    depthList = []
                    levelDepth += 1
            else:
                finalLevel = levelDepth
                levelDepth = float('inf')
        else:
            if len(openLists) == 0:
                openLists = depthList
                depthList = []
                levelDepth += 1
    toc = time.perf_counter()
    print(f"Runtime: {toc - tic:0.4f} seconds")
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')
    return 0

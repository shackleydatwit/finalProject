#!/usr/bin/python
import sys

file = None 
columns = None
rows = None
botLocation = None
generated = 0
expanded = 0
sampleLocations = []
blockedLocations = []
openLists = []
children = []
hashList = []
def depthFirstSearch(): 
    global openLists, hashList, generated, expanded
    openLists.append(botLocation)
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
                #left
                if(node[1]-1 >= 0 and not (node[1]-1 in blockedLocations[node[0]] )):
                    if not[node[0], node[1]-1] in openLists:
                        children.insert(0, [node[0], node[1]-1])
                        generated += 1
                        print('L')
                #right
                if(node[1]+1 < columns and not (node[1]+1 in blockedLocations[node[0]] )):
                    if not[node[0], node[1]+1] in openLists:
                        children.insert(0, [node[0], node[1]+1])
                        generated += 1
                        print('R')
                #up
                if(node[0]-1 >= 0 and not (node[1] in blockedLocations[node[0]-1] )):
                    if not[node[0]-1, node[1]] in openLists:
                        children.insert(0, [node[0]-1, node[1]])
                        generated += 1
                        print('U')
                #down
                if(node[0]+1 < rows and not (node[1] in blockedLocations[node[0]+1] )):
                    if not[node[0]+1, node[1]] in openLists:
                        children.insert(0, [node[0]+1, node[1]])
                        generated += 1
                        print('D')
                temp = children + openLists
                openLists=temp
            else:
                notFoundAll = False
    print(generated, 'nodes generated', '\n',expanded, 'nodes expanded')
    return 0
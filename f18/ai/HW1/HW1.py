
def search(problem):
    frontier = [problem]
    explored = []
    while True:
        if len(frontier) == 0:
            return "end of frontier"
        node = frontier.pop()
        if isGoal(node):
            
            return explored
            #return the path
        explored.append(node)
        
        for i in range(0,9):
            toAppend = toggle(node, i)
            if toAppend not in frontier and toAppend not in explored:
                frontier.append(toAppend)
                

def helper():
    explored_nodes = search("DEDEEEDED")
    return explored_nodes

def toggle(node, pos):
    neighbors = getNeighbors(pos)
    for neighbor in neighbors:
        node = switchGem(node, neighbor)
    return node
            
        
        
def switchGem(myList, pos):
    gem = myList[pos]
    
    if gem == 'E':
        gem = 'D'
    elif gem == 'D':
        gem = 'R'
    elif gem == 'R':
        gem = 'E'
    else:
        raise ValueError("Invalid gem type.")
    newList = myList[:pos] + gem + myList[(pos+1):]
    return newList

def getNeighbors(pos):
    positions = [pos]
    
    #left
    if (pos % 3) == 0:
        positions.append(pos+1)
    #middle
    elif (pos % 3) == 1:
        positions.append(pos-1)
        positions.append(pos+1)
    #right
    elif (pos % 3) == 2:
        positions.append(pos-1)
    else:
        raise ValueError("Position out of range.")

    #top
    if pos < 3 and pos >= 0:
        positions.append(pos+3)
    #middle
    elif pos < 6 and pos >= 3:
        positions.append(pos+3)
        positions.append(pos-3)
    #bottom
    elif pos < 9 and pos >= 6:
        positions.append(pos-3)
    else:
        raise ValueError("Position out of range.")
 
    return positions

    
def isGoal(node):
    if node == "EEEEEEEEE" or node == "DDDDDDDDD" or node == "RRRRRRRRR":
        return True
    else:
        return False
    
    

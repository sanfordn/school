from collections import deque
 
 
def get_neighbors( state ):
    #neighbors = []
    neighbors = deque()
    for index, letter in enumerate(state):
        upOne = str((int(letter) + 1) % 10)
        downOne = str(((int(letter) + 10) - 1)%10)
        neighbors.append(state[:index] + upOne + state[index + 1:])
        neighbors.append(state[:index] + downOne + state[index + 1:])
    return neighbors
 
 
def bfs( current, goal, forbiddens ):
    frontier = []
    frontier.append((current, 0))
    frontier = deque(frontier)
    visited = []
    visited = deque(visited)
    solved = False
 
    while len(frontier) > 0:
        state, steps = frontier.popleft()
        if state == goal:
            print( steps )
            solved = True
            break
 
        visited.append( state )
 
        for neighbor in get_neighbors( state ):
            if neighbor not in visited and neighbor not in forbiddens:
                frontier.append( (neighbor, steps + 1) )
 
    if not solved:
        print( -1 )
 
 
def main( ):
    cases = int(input())
 
    for _ in range(cases):
        current = "".join(input().split())
        goal = "".join(input().split())
 
        num_forbidden = int(input())
        print(num_forbidden)
        #forbiddens = []
        forbiddens = deque()
 
        for _ in range(num_forbidden):
            forbiddens.append("".join(input().split()))
        input()
        bfs( current, goal, forbiddens )
 
 
if __name__ == '__main__':
    main( )

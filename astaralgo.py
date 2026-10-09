import heapq   #heapq helps us select the node with the smallest f(n).

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_cost, current_node)
    open_list = [(0, start)]

    # Cost from start node to each node
    g_cost = {node: float('inf') for node in graph}  #loat('inf') in Python means positive infinity (∞).
    g_cost[start] = 0

    # To reconstruct the final path
#Create the parent dictionary eg parent['B'] = 'A'
    parent = {node: None for node in graph}

    while open_list:
        # Select node with minimum f(n)
        current_f, current = heapq.heappop(open_list) #Initially:It Contains (0, A)
        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]
#The path initially becomes:E, D, C, B, A
            path.reverse()
            return path, g_cost[goal]

        # Explore neighboring nodes
        for neighbor, cost in graph[current]:   #Current node is A.
     #Acco rding to the graph: ‘A': [('B', 1), ('C', 4)]


            # Calculate new actual cost
            new_g_cost = g_cost[current] + cost    #g(A) = 0, cost(A,B) = 1, so g(B)=0+1=1

            # Check whether this is a better path
            if new_g_cost < g_cost[neighbor]: #g(B)=infinity, so 1<infinity
                g_cost[neighbor] = new_g_cost # update g(B)=1 
                parent[neighbor] = current # store parent, parent[B] = A
# Calculate f(n)
                # f(n) = g(n) + h(n)
                f_cost = new_g_cost + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor)) #open_list = [(7, B)] # now consider C now open_list = [(6, C), (7, B)]

    return None, float('inf')


# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1), ('E', 3)],
    'E': [('D', 3)]
}

# Heuristic values h(n)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

# Starting and goal nodes
start = 'A'
goal = 'E'

# Execute A* algorithm
path, cost = a_star(graph, heuristic, start, goal)

# Display result
if path:
    print("Optimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found.")

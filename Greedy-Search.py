import heapq

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 42, 'D': 15},
    'C': {'B':42, 'E': 8},
    'D': {'E':5, 'F': 15},
    'E': {'F': 5, 'D': 5},
    'F': {}
}

h = {
    'A': 25,
    'B': 8,
    'C': 20,
    'D': 6,
    'E': 12,
    'F': 0
}

def greedy_best_first_search(start, goal):
   
    open_list = [(h[start], start)]
  
    closed = set()
    came_from = {}

    # repeat
    while open_list:
       
        _, current = heapq.heappop(open_list)

        if current in closed:
            continue

        closed.add(current)

        
        if current == goal:
            break


        for neighbor in graph[current]:
           
            if neighbor not in closed:
                heapq.heappush(open_list, (h[neighbor], neighbor))
                if neighbor not in came_from:
                    came_from[neighbor] = current


    path = []
    node = goal
    while node != start:
        path.append(node)
        node = came_from.get(node)
        if node is None:
            return ["No Path Found"], closed
    path.append(start)
    path.reverse()

    return path, closed

# تست:
path, closed = greedy_best_first_search('A', 'F')
print("Final Path:", path)
print("Closed", closed)

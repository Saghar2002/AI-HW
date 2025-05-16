import heapq

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 42, 'D': 15},
    'C': {'B':42, 'E': 8},
    'D': {'E':5, 'F': 15},
    'E': {'F': 5, 'D': 5},
    'F': {}
}

def uniform_cost_search(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost_so_far = {start: 0}
    closed = set()

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current == goal:
            break

        if current in closed:
            continue
        closed.add(current)

        for neighbor in graph[current]:
            new_cost = current_cost + graph[current][neighbor]
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(open_list, (new_cost, neighbor))
                came_from[neighbor] = current

    # ساخت مسیر نهایی
    path = []
    node = goal
    if node not in came_from and node != start:
        print("No path found")
        return
    while node != start:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path.reverse()

    print("Final path:", path)
    print("Total path cost:", cost_so_far[goal])
    print("Closed set:", closed)

uniform_cost_search('A', 'F')

import heapq

graph = {
    'A': {'B': 10, 'C': 3},
    'B': {'C': 42, 'D': 15},
    'C': {'B':42, 'E': 8},
    'D': {'E':5, 'F': 15},
    'E': {'F': 5, 'D': 5},
    'F': {}
}


h_values = {
    'A': 25,
    'B': 8,
    'C': 20,
    'D': 6,
    'E': 12,
    'F': 0
}

def a_star(start, goal):
    open_list = []
    heapq.heappush(open_list, (h_values[start], start))  # (f(n), node)
    
    came_from = {}
    g_cost = {start: 0}  # هزینه واقعی تا این گره
    f_cost = {start: h_values[start]}  # هزینه کل: g(n)+h(n)
    closed = set()

    while open_list:
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            break

        if current in closed:
            continue
        
        closed.add(current)

        for neighbor in graph[current]:
            new_g_cost = g_cost[current] + graph[current][neighbor]
            if neighbor not in g_cost or new_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_g_cost
                f_cost[neighbor] = new_g_cost + h_values[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))
                came_from[neighbor] = current

    # ساخت مسیر از هدف به شروع
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
    print("Total path cost:", g_cost[goal])
    print("Closed set:", closed)

# اجرای الگوریتم
a_star('A', 'F')

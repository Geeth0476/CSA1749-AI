from itertools import permutations

# Function to calculate the total distance of a given path
def calculate_total_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    # Add the distance to return to the starting city
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

# Brute-force solution for TSP
def travelling_salesperson_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    shortest_path = None
    min_distance = float('inf')
    
    # Generate all possible paths (permutations of cities)
    for path in permutations(cities):
        current_distance = calculate_total_distance(path, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = path
    
    return shortest_path, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

shortest_path, min_distance = travelling_salesperson_brute_force(distance_matrix)
print("Shortest path:", shortest_path)
print("Minimum distance:", min_distance)
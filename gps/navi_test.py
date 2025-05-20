import osmnx as ox
import networkx as nx
import math

# take the latitude and longitude values from the gps
def calculate_bearing(lat1, lon1, lat2, lon2):
    difference_lon = lon2 - lon1
    y = math.sin(difference_lon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(difference_lon)
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360
    return bearing

# use the lat/long calculation to get the direction of movement
def get_direction(bearing):
    directions = ["north", "northeast", "east", "southeast", "south", "southwest", "west", "northwest"]
    index = round(bearing / 45) % 8
    return directions[index]

# 
def generate_directions(graph, route):
    directions = []
    total_distance = 0

    for i in range(1, len(route)):
        start_node = route[i - 1]
        end_node = route[i]
        edge = graph[start_node][end_node][0]

        start_lat, start_lon = graph.nodes[start_node]['y'], graph.nodes[start_node]['x']
        end_lat, end_lon = graph.nodes[end_node]['y'], graph.nodes[end_node]['x']

        bearing = calculate_bearing(start_lat, start_lon, end_lat, end_lon)
        direction = get_direction(bearing)

        street_name = edge.get('name', 'Unnamed street')
        distance = edge['length']
        total_distance += distance

        if i == 1:
            directions.append(f"Start by heading {direction} on {street_name} for {distance:.0f} meters")
        else:
            prev_edge = graph[route[i-2]][route[i-1]][0]
            prev_name = prev_edge.get('name', 'Unnamed street')
            
            if prev_name != street_name:
                turn_direction = "left" if (bearing - prev_bearing + 360) % 360 > 180 else "right"
                directions.append(f"Turn {turn_direction} onto {street_name} and continue for {distance:.0f} meters")
            else:
                directions.append(f"Continue on {street_name} for {distance:.0f} meters")

        prev_bearing = bearing

    directions.append(f"You have reached your destination. Total distance: {total_distance:.0f} meters")
    return directions

# Generate directions based on the route
directions = generate_directions(graph_seattle, route)

# Print out the directions
for step in directions:
    print(step)

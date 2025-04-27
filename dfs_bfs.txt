
graph = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6'],
    '4': [],
    '5': ['6'],
    '6': []
}

visited=[]
queue = []

# BFS Implementation
def breadthFirstSearch(visited, graph, node):

    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)  
        print(m, end=" ")  

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Breadth-First Search:")
#visited_bfs = []  
breadthFirstSearch(visited, graph, '1')

#DFS Implementation
visited_dfs = set()  

def depthFirstSearch(visited, graph, node):
    if node not in visited:
        print(node, end=" ")  
        visited.add(node)
    for neighbour in graph[node]:
            depthFirstSearch(visited, graph, neighbour)

print("\nDepth-First Search:")
depthFirstSearch(visited_dfs, graph, '1')


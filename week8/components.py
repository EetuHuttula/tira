def find_components(nodes, edges):
    graph = {node: [] for node in nodes}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    sub_list = []

    def dfs(node, sub_list):
        visited.add(node)
        sub_list.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                dfs(next_node, sub_list)
    
    for node in nodes:
        if node not in visited:
            ssub_list = []
            dfs(node, ssub_list)
            sub_list.append(sorted(ssub_list)) 
    
    return sorted(sub_list, key=min)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]
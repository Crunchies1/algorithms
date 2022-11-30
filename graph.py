from collections import defaultdict, deque

def furthestNode(nodes):
    graph = defaultdict(list)
    roomNumbers = []
    for node in nodes:
        graph[node[0]].append(node[1]) 
        graph[node[1]].append(node[0]) # Comment out if not bidirectional
        if node[0] not in roomNumbers:
            roomNumbers.append(node[0])
        if node[1] not in roomNumbers:
            roomNumbers.append(node[1])

    return BFS(graph, roomNumbers, 0)
    
def BFS(graph, nodes, startNode):
        visitedIndex = {nodes[i] : False for i in range(len(nodes))}
        distances = {nodes[i] : -1 for i in range(len(nodes))}
        queue = deque()
 
        distances[startNode] = 0
        queue.append(startNode)
        visitedIndex[startNode] = True
 
        while queue:
            front = queue.popleft()
            
            for i in graph[front]:
                if not visitedIndex[i]:
                    visitedIndex[i] = True
                    distances[i] = distances[front] + 1
                    queue.append(i)
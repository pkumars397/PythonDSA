def nodes_at_distance(graph,start,distance):
    visited=set()
    queue=[(start,0)]
    result=[]
    while queue:
        current,dist=queue.pop(0)
        if dist==distance:
            result.append(current)
        elif dist<distance:
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor,dist+1))
    return result
g={0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
print(nodes_at_distance(g,0,2))
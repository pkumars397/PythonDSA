def pathCheck(graph,start,end,visited=None):
    if visited is None:
        visited=set()
    if start==end:
        return True
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            if pathCheck(graph,neighbor,end,visited):
                return True
    return False

g={0:{1,2},1:{0,3},2:{0,3},3:{1,2}}
print(pathCheck(g,0,3))
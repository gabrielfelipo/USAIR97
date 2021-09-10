def Graph(arestas, vertices):
    adj=[]
    distance=[]
    for i in range(vertices):
        adj.append([])
        distance.append([])
    for u, v, w in arestas:
        adj[u].append(v)
        adj[v].append(u)
        distance[u].append(w)
        distance[v].append(w)
    
    return adj, distance
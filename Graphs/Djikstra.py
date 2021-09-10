def Djikst(grafo, distancia, s, w):
    
    visited=[]
    p=[]
    c=[]
    for i in range(len(grafo)):
        visited.append(False)
        p.append(float("inf"))
        c.append(-1)

    queue = []
    pesos = []
    c[s]=str(s)
    p[s]=0
    queue.append(s)
    pesos.append(p[s])
    visited[s] = True
    aux=s
    while queue:
        menor=buscarLocalMenor(pesos)
        pesos.pop(menor)
        s = queue.pop(menor)

        for i in range (len(grafo[s])):
            if p[s]+distancia[s][i]<p[grafo[s][i]]:
                p[grafo[s][i]]=p[s]+distancia[s][i]
                c[grafo[s][i]]=str(c[s]+' '+str(grafo[s][i]+1))
            if visited[grafo[s][i]] == False:
                queue.append(grafo[s][i])
                pesos.append(p[grafo[s][i]])
                visited[grafo[s][i]] = True

    return p[w], c[w]

def buscarLocalMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return lst.index(i)
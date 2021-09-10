from Graphs import Grafo
def Dijkstra(grafo, distancia, s, w):

    visited=[]
    p=[]
    c=[]
    for i in range(len(grafo)):
        visited.append(False)
        p.append(float("inf"))
        c.append(-1)

    queue = []
    pesos = []
    c[s]=str(s+1)
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

    return p, c        

def buscarLocalMenor(lst):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return lst.index(i)

vertices=332
arestas=[]
aeroportos=[]


for i in range(vertices):
    a=input().split()
    aeroportos.append(a[1])
inicial=int(entrada[1])
final=int(entrada[2]) 
while True:
    try:
        entrada=input()
        x= entrada.split()
        x[0]=int(x[0])-1
        x[1]=int(x[1])-1
        x[2]=float(x[2])
        arestas.append(x)

    except:
        break
        
        
grafo = Grafo(arestas,vertices)

x=Dijkstra(grafo.adj, grafo.distance, inicial-1, final-1)
print(x[0][5])
print(x[1][5])
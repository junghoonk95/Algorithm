parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0

def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
        
    return parent[v]

def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):    
    for v in graph['vertices']:
        make_set(v)
    
    mst = []
    
    edges = graph['edges']
    edges.sort()
    
    for edge in edges:
        weight, v, u = edge
                
        if find(v) != find(u):
            union(v, u)
            mst.append(edge)
    
    return mst
            
n=int(input())
m=int(input())
ver=[]
ed=[]
for i in range(1,n+1):
   ver.append(i)

for i in range(m):
    a,b,c=map(int,input().split())
    ed.append((c,a,b))


graph = {
'vertices': ver,
'edges': ed
}

sum=0
result=(kruskal(graph))
for i in result:
    sum+=i[0]
print(sum)

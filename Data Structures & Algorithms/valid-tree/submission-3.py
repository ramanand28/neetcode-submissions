class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self,node):
        curr = node
        while curr != self.parent[curr]:
            curr = self.parent[curr]
        return curr
    
    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)
        if pv == pu:
            return False
        if self.rank[pu] > self.rank[pv]:
            pv, pu = pu, pv
        self.parent[pu] = pv
        self.rank[pv] += self.rank[pu]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds = DSU(n)
        comp = n
        for u, v in edges:
            if not ds.union(u,v):
                return False
            comp -= 1
        return comp == 1
        
        
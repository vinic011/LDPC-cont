class Edge:
    def __init__(self,idx_c,idx_v):
        self.m=0
        self.idx_c=idx_c
        self.idx_v=idx_v
    
    def reset(self):
        self.m=0
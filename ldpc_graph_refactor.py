from node import CNode, VNode
from edge import Edge
import numpy as np

class LdpcGraphRefactor:
    def __init__(self,max_iterations:int):
        self.c:list[CNode]=[]
        self.v:list[VNode]=[]
        self.max_iterations=max_iterations
        
    def process(self,llr:np.ndarray):
        for _ in range(self.max_iterations):
            for n in range(len(self.v)):
                self.v[n].message(llr[n])
            #Parallel(n_jobs=10)(delayed(self.v[n].message)(llr[n]) for n in range(len(self.v)))
            found=False
            for m in range(len(self.c)):
                if not self.c[m].check():
                    found=True
                    break
            if not found:
                break
            for c in self.c:
                c.message()
            #Parallel(n_jobs=10)(delayed(c.message)() for c in self.c)
        return np.array([self.v[i].final_llr(llr[i]) for i in range(len(self.v))])
    
    def reset(self):
        for v in self.v:
            v.reset()
        #Parallel(n_jobs=10)(delayed(v.reset)() for v in self.v)



def from_matrix(H:np.ndarray,max_iterations):
        H = H.copy()
        g=LdpcGraphRefactor(max_iterations)
        for i in range(H.shape[0]):
            g.c.append(CNode(i))
        for i in range(H.shape[1]):
            g.v.append(VNode(i))
            for d in list(np.argwhere(H[:,i].flatten())):
                e=Edge(int(d),i)
                g.c[int(d)].add_edge(e)
                g.v[i].add_edge(e)
        return g
        



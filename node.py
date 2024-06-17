import numpy as np
from edge import Edge
from abc import ABC,abstractmethod

class Node:
    def __init__(self,idx) -> None:
        self.edges:list[Edge]=[]
        self.idx=idx

    def add_edge(self,e:Edge):
        self.edges.append(e)

    def reset(self):
        for e in self.edges:
            e.reset()

class VNode(Node):
    def final_llr(self,llr):
        return self.l_f

    def message(self,llr):
        l_e=np.array([e.m for e in self.edges])
        self.l_f=llr+np.sum(l_e)
        for i in  range(len(self.edges)):
            self.edges[i].m=self.l_f-l_e[i]
    

class CNode(Node):
    def check(self):
        return np.prod([e.m for e in self.edges])>0

    def message(self):
        l_e=np.array([e.m for e in self.edges])
        for i in range(len(l_e)):
            self.edges[i].m=self._processed_index(i,l_e)

    def _processed_index(self,index,llrs):
        llrs = llrs.copy()
        x=np.delete(llrs, index)
        module = np.min(np.absolute(x))
        sign=np.prod(np.sign(x))
        return sign*module

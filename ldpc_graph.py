import numpy as np
import random
import decision as decision
import cnode as cnode
from parity_matrix import generate_matrix

#perhaps it will be necessary to change this function
class LDPC_Graph:
    def __init__(self,N:int,dv:int,dc:int,max_iterations:int):
        #TODO: insert here algorithm to build the graph in a random manner or whatever way its best
        self.N=N
        self.dv=dv
        self.dc=dc
        self.M=N*dv//dc
        self.matrix=generate_matrix(N,dv,dc)
        self._graph=[[]]*self.matrix.shape[0]
        for i in range(self.matrix.shape[0]):
            self._graph[i]=np.argwhere(self.matrix[i]).flatten()
        self.max_iterations=max_iterations
    
    def process(self,llr:np.ndarray):
        V_to_C=np.zeros(self.matrix.shape)
        C_to_V=np.zeros(self.matrix.shape)
        for i in range(self.max_iterations):
            for n in range(self.N):
                index_list=np.argwhere(self.matrix[:,n])
                V_to_C[index_list,n]=llr[n]+np.sum(C_to_V[index_list,n])-C_to_V[index_list,n]
            valid_c=0
            for m in range(self.M):
                index_list=np.argwhere(self.matrix[m])
                if np.prod(V_to_C[m,index_list])>0:
                    valid_c+=1
            if valid_c==self.M:
                break
            for m in range(self.M):
                index_list=np.argwhere(self.matrix[m])
                llr_i=V_to_C[m,index_list]
                C_to_V[m,index_list]=cnode.process_cnode(llr_i)[:,None]


        l_f=llr+np.sum(C_to_V,axis=0)

        #decisions = [decision.decision(llr[n],V_to_C[np.argwhere(self.matrix[:,n]),n]) for n in range(self.N)]
        return l_f
        #decides
    
    
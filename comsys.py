import numpy as np
from gaussian_channel import Gaussian_Channel
from ldpc_graph_refactor import LdpcGraphRefactor

class ComSys:
    def __init__(self,channel:Gaussian_Channel,graph:LdpcGraphRefactor):
        self.channel=channel
        self.graph=graph

    def __call__(self,arr:np.ndarray):
        arr = arr.copy()
        #transmits a array (with encoding and decoding) using the equaivalent modulation
        if len(arr.shape)==1:
            arr=arr[None,:]
        s=np.zeros(arr.shape[0])
        for u in range(arr.shape[0]):
            self.graph.reset()
            #print(u)
            r=self.channel(self.modulate(arr[u]))
            llr=self.channel.llr(r)
            llr_f=self.graph.process(llr)            
            out=self.decide(llr_f)
            s[u]=np.sum(out)
        return np.sum(s)/arr.size

    def modulate(self,arr):
        return -2*arr+1
    
    def decide(self,llr):
        return (llr<0).astype(int)
    
    
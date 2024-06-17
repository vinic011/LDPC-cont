import numpy as np
def process_cnode(llrs):
    return np.array([processed_index(i,llrs) for i in range(len(llrs))])

def processed_index(index, llrs):
    llrs = llrs.copy()
    x=np.delete(llrs, index)
    module = np.min(np.absolute(x))
    sign=np.prod(np.sign(x))
    return sign*module


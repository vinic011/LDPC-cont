import random
import numpy as np
def generate_matrix(N,dv,dc):
    M=(N*dv)//dc
    matrix=np.array([[0]*N]*M)
    count=np.zeros(M)
    for n in range(N):
        used=[]
        for u in range(dv):
            minimum=np.min(count)
            available=list(np.argwhere(count==minimum).flatten())
            candidates=[i for i in available if i not in used]
            index=random.choice(candidates)
            count[index]+=1
            used.append(index)
            matrix[index,n]=1
    return matrix
            
                

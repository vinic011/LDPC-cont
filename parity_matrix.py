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
            
def write_csv(H,filename):
    x=np.argwhere(H.T)[:,None,1]+1
    y=np.reshape(x,(-1,3))
    rows = ["{},{},{}".format(i, j, k) for i, j, k in y] 
    text = "\n".join(rows)
    with open('graph.csv', 'w') as f: 
        f.write(text)

def from_csv(filename):
    with open("graph.csv",'r') as g:
        s=g.read()
    a=s.split('\n')
    numbers=[[[i,int(n)-1] for n in a[i].split(',')] for i in range(len(a))]
    index=list(np.array(numbers).reshape(-1,2))
    H=np.zeros((1001, 429))
    for i in index:
        H[i[0],i[1]]=1
    return H.T.astype(np.int16)
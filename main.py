import ldpc_graph_refactor as ldpc
from comsys import ComSys
import numpy as np
import gaussian_channel
import parity_matrix
import pandas as pd
from joblib import Parallel, delayed
import matplotlib.pyplot as plt
import random


random.seed(20) #just for reproductability
#H = parity_matrix.generate_matrix(1001,3,7)
#m=np.argwhere(H)
H=parity_matrix.from_csv("graph.csv")
def process(snr):
    y=np.zeros((1000,1001))
    graph=ldpc.from_matrix(H,20)
    #graph=ldpc_graph.LDPC_Graph(H,25)
    channel = gaussian_channel.Gaussian_Channel(snr)
    sys=ComSys(channel,graph)
    return snr,sys(y)

probs_snr = Parallel(n_jobs=11)(delayed(process)(snr) for snr in np.arange(0,5.1,0.5))
snrs = [p[0] for p in probs_snr]
probs = [p[1] for p in probs_snr]
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(2, 1, 1)
line, = ax.plot(snrs, probs)
ax.set_ylabel('Bit error prob')
ax.set_xlabel('SNR')
ax.set_yscale('log')
fig.savefig("teste.png")

import numpy as np
class Gaussian_Channel:
    def __init__(self,SNR:float)->None:
        sigma2=0.5*10**(-SNR/10)
        self._std=np.sqrt(sigma2)

    def __call__(self,arr:np.ndarray)->np.ndarray:
        return np.random.normal(0,self._std,arr.shape)+arr
    
    def llr(self,arr:np.ndarray):
        return 2*arr/(self._std**2)
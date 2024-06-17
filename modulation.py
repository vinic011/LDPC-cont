import numpy as np

class Modulation:
    def __init__(self,A:float):
        self.Ad=A

    def to_mod(self,arr:np.ndarray)->np.ndarray:
        return self.Ad*(arr-0.5)
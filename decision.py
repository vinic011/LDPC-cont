import numpy as np

def decision(in_llr, out_llrs):
    decision_sum = in_llr + np.sum(out_llrs)
    return int(decision_sum <= 0)
def be_0_probability(in_llr, out_llrs):
    decision_sum = in_llr + np.sum(out_llrs)
    return 1 / (1 + np.exp(-decision_sum))

def be_1_probability(in_llr, out_llrs):
    decision_sum = in_llr + np.sum(out_llrs)
    return 1 / (1 + np.exp(decision_sum))
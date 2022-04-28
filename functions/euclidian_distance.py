import numpy as np

def compute(ptA,ptB):
	dist = np.linalg.norm(ptA - ptB)
	return dist
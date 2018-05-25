import numpy as np
from scipy.linalg import solve

def count(list1,list2,list3):
    a = np.array(list1,list2,list3 )
    b = np.array(list3)
    x = solve(a, b)
    print(x)

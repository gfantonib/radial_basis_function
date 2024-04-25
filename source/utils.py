import numpy as np
import pandas as pd

def generate_random_arrays_df(n, m, a, b):
    arrays = [np.random.uniform(a, b, size=m) for _ in range(n)]
    df = pd.DataFrame(arrays)
    return df
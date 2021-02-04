##### 解けた #####

import numpy as np

S=np.asarray(list(input()))

print(len(np.where(S=="A")[0]),len(np.where(S=="B")[0]),
len(np.where(S=="C")[0]),len(np.where(S=="D")[0]),
len(np.where(S=="E")[0]),len(np.where(S=="F")[0]))
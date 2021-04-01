import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 生成数据
v1 = np.random.normal(0, 1, 100)
v2 = np.random.randint(0, 23, 100)
v3 = v1 * v2

# 3*100 的数据框
df = pd.DataFrame([v1, v2, v3]).T
# 绘制散点图矩阵
pd.plotting.scatter_matrix(df)
plt.show()

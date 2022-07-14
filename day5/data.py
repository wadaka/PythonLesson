import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import random

#項目:体重のある、空の配列を作成
df = pd.DataFrame(columns=['体重'])

for i in range(1,32):
    weight=(random.uniform(60,63))
    df.loc[str(i)+'日']=weight

df.plot()
plt.grid()
plt.show()

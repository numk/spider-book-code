# 对应：第5章 数据存储
# 小节：5.1 文件存储
# 条目：5.1.2 CSV 文件的存储
# 清单：07
# 说明：摘自书稿示例，未改写。

import pandas as pd

# 将列表数据转为 DataFrame，然后写入 CSV
df = pd.DataFrame(data[1:], columns=data[0])   # data[0] 作为表头
df.to_csv('data_pandas.csv', index=False, encoding='utf-8')

# 读取 CSV 文件
df_read = pd.read_csv('data.csv')
print(df_read)

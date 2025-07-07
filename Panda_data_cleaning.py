import pandas as pd

# 第三个日期格式错误
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())


# 示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, None, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)

x=df['Age'].mean()  # 计算均值
df.fillna({'Age': x}, inplace=True)# 填充缺失的 "Age" 为均值

print(df)


from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

#标准化数据

# 示例数据
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}

df = pd.DataFrame(data)
# 标准化数据
scaler = StandardScaler()

scaler.fit(df)
df_scaled = scaler.transform(df)
#一步到位 直接转换为标准化数据 df_scaled = scaler.fit_transform(df)

print(df_scaled)

# 归一化数据
scaler = MinMaxScaler(feature_range=(0, 1))  # 默认即为 [0,1]

scaler.fit(df)
df_normalized = scaler.transform(df)
#一步到位 df_normalized = scaler.fit_transform(df)

print(df_normalized)

import pandas as pd
import os

nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
     
df = pd.DataFrame(dict)

# 打印 dataframe
print(df)

# 保存 dataframe
df.to_csv('site.csv')

# 更改工作目录到 h:\VS_code\ML_Study\
os.chdir('h:/VS_code/ML_Study/test_files')
print("当前工作目录:", os.getcwd())
# 读取 Excel 文件
file_path = 'nba.csv'
if os.path.exists(file_path):
    df_nba = pd.read_csv(file_path)
    print(df_nba)
else:
    print(f"文件 {file_path} 不存在。请检查文件路径。")

print(df_nba.head(10))
print(df_nba.tail(10))
print(df_nba.info())



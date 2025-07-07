import pandas as pd
import os

# 更改工作目录到 h:\VS_code\ML_Study\
os.chdir('h:/VS_code/ML_Study/test_files')
print("当前工作目录:", os.getcwd())
# 读取 Excel 文件
file_path = 'Panda_test.xlsx'
if os.path.exists(file_path):
    ds = pd.read_excel(file_path)
    print(ds)
else:
    print(f"文件 {file_path} 不存在。请检查文件路径。")

ds = pd.read_excel('Panda_test.xlsx', header=None, names=['name', 'age', 'city'], skiprows=2)
print(ds)



nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}

# 创建一个简单的 DataFrame
name_excel = pd.DataFrame(dict)

name_excel['Row Number'] = range(1, len(name_excel) + 1)

name_excel = name_excel[['Row Number'] + list(name_excel.columns[:-1])]

# 将 DataFrame 写入 Excel 文件，写入 'Sheet1' 表单
name_excel.to_excel('name.xlsx', sheet_name='1', index=False, header = 1)


# 写入多个表单，使用 ExcelWriter
with pd.ExcelWriter('name.xlsx') as writer:
    name_excel.to_excel(writer, sheet_name='1', index=False, header = 1)
    name_excel.to_excel(writer, sheet_name='2', index=False, header = 1)

print(name_excel)

name_excel = name_excel.drop(columns=['Row Number'])

print(name_excel)


from datetime import date, datetime  
df = pd.DataFrame(
    [
        [date(2025, 1, 31), date(2001, 6, 14)],
        [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],
    ],
    index=["Date", "Datetime"],
    columns=["X", "Y"],
)  
with pd.ExcelWriter(
    "path_to_file.xlsx",
    date_format="YYYY-MM-DD",
    datetime_format="YYYY-MM-DD HH:MM:SS"
) as writer:
    df.to_excel(writer)

print(df)





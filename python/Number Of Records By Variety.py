import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Number Of Records By Variety\dataset\\Number Of Records By Variety.xlsx')
df1 = df.pivot_table(index='variety', values='sepal_length', aggfunc='count')
df1 = df1.rename(columns={'sepal_length': 'count'})


print(df1.sort_values(by='variety',ascending=True))

df2 = df.groupby('variety')['variety'].count().reset_index(name='count')
print(df2.sort_values(by='variety',ascending=True))
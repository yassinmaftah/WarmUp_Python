import pandas as pd


df = pd.read_csv('raw_users.csv')

print(df)
# print(df.info())

print(df)
# print(df)
df.drop_duplicates(subset=['name'],keep='first',inplace=True)
df['points'] = df['points'].fillna(0)
df['email'] = df['email'].fillna("no_email_provided")
print("*" * 50)
print(df)
df.dropna(subset='join_date',inplace = True)
print("*" * 50)
print(df)


# df.to_csv('clean_data.csv',index=False)
df.to_excel('clean_data.xlsx',index=0)
# print(df[['name','email']])
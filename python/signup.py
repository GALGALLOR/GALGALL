import pandas as pd
df = pd.DataFrame(columns = ['name','pass'])
name = input('what is your name? ')
passw = input('get yourself  a password ')
for num in range(1):
    df.loc[num]=[name,passw]

df.to_excel(name+'.xlsx', sheet_name='Sheet1')
df = pd.read_excel(name+'.xlsx')
print(df)

print('now log in')


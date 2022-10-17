import pandas as pd

t1 = pd.read_excel("teste_1.xlsx")
t2 = pd.read_excel("teste_2.xlsx")
t3 = pd.read_excel("teste_3.xlsx")
t4 = pd.read_excel("teste_4.xlsx")

all_df_list = [t1, t2, t3, t4]


appended_df = pd.concat(all_df_list)


appended_df.to_excel("pivot.xlsx", index=False)
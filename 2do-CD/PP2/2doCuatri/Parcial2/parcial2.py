import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("pedidos_cafeteria.csv")

# df.info()

#! Preg 4
# print((df.isna().mean() * 100).round(1))

#! Preg 5
# print(df.isna().sum(axis=1).idxmax())

#! Preg 6
# print(len(df.dropna()))

#! Preg 10
# print(df.groupby("sucursal")["puntaje"].agg(["mean", "count"]))

#! Preg 21
# print(sns.boxplot(data=df, y="edad_cliente"))
# plt.show()

#! Preg 22
# q1 = df["cantidad"].quantile(0.25)
# q3 = df["cantidad"].quantile(0.75)
# iqr = q3 - q1
# limite_sup = q3 + 1.5 * iqr

# print(limite_sup)

# superan = (df["cantidad"] > limite_sup).sum()
# print(superan)


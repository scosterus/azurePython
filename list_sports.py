from turtle import clear
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("static/media/Toughest Sport by Skill.xlsx")

bp_endurance = plt.boxplot(data["Endurance"])
q1 = [round(min(item.get_ydata()), 1) for item in bp_endurance['boxes']]
q3 = [round(max(item.get_ydata()), 1) for item in bp_endurance['boxes']]

print(f'Q1: {q1}\n'
      f'Q3: {q3}')

data_endurance_beg = data[data["Endurance"] <= q1[0]]
data_endurance_mid = data[(data["Endurance"] > q1[0]) & (data["Endurance"] < q3[0])]
data_endurance_pro = data[data["Endurance"] >= q3[0]]

endurance_beg = data_endurance_beg["Sport"].tolist()
endurance_mid = data_endurance_mid["Sport"].tolist()
endurance_pro = data_endurance_pro["Sport"].tolist()
print(endurance_beg)
print()
print(endurance_mid)
print()
print(endurance_pro)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme()
sns.set(font_scale=1.4)
plt.rcParams.update({'font.size': 32})

x0 = np.linspace(0, 2.5, 100)
df = pd.read_csv('Comp.csv')
x2, y2 = [], []
for x, y in zip(df['dist1'], df['dist2']):
    if x < 0.001:
        x2.append(x)
        y2.append(y)
fig = plt.figure(figsize=(6,5))
ax1 = fig.add_subplot(111)
ax1.scatter(df['dist1'], df['dist2'], s=5)
ax1.scatter(x2, y2, s=5, c='g')

ax1.set_ylabel('Distortion (This work)')
ax1.set_xlabel('Distortion (Smidt et al)')
ax1.yaxis.label.set_color('r')
ax1.xaxis.label.set_color('b')
ax1.plot(x0, x0, '--k', alpha=0.3)
ax1.tick_params(axis='y', colors='r')
ax1.tick_params(axis='x', colors='b')
plt.tight_layout()
ax1.set_xlim(-0.1, 2.3)
ax1.set_ylim(-0.1, 2.3)

plt.savefig('Fig2-validation.pdf')

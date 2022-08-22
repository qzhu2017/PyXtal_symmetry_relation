import pandas as pd
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pyxtal import Group
from matplotlib.gridspec import GridSpec
from pymatgen.core.composition import Composition


sns.set_theme()
sns.set(font_scale=1.4)
#plt.rcParams.update({'font.size': 32})

df = pd.read_csv('2022_all_pairs.csv')
stois = np.zeros(8)
for formula in df['formula']:
    comp = Composition(formula)
    stois[len(comp.elements)] += 1
    #if len(comp) == 1 or len(comp)==5:
    #    print(formula)

print(stois)

d_tol, e_tol = 1.0, 0.2
de = df['de']
dists = df['dist']
count1, count2, count3 = 0, 0, 0
for e, d in zip(de, dists):
    if d<d_tol and abs(e)<e_tol:
        count1 += 1
    if abs(e)<e_tol:
        count2 += 1
    if d<d_tol:
        count3 += 1
print("Good", count1, count1/len(de))
print("de", count2, count2/len(de))
print("dist", count3/len(dists))
fig = plt.figure(figsize=(18, 8))
#widths = [1.8, 1.5, 1.5, 1.8]
widths = [1.8, 1.5, 1.5]
heights = [2, 2]
gs = fig.add_gridspec(ncols=3, nrows=2, width_ratios=widths,
                          height_ratios=heights)

#gs = GridSpec(2, 4)
axs = fig.add_subplot(gs[0, 0])
#ax0 = fig.add_subplot(gs[0, 3])
ax1 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax2 = fig.add_subplot(gs[1, :])

#==============================================
n, bins, patches = ax1.hist(df['dist'], 50, density=False, color='r')
ax1.set_xlim(0, 1.8)
ax1.set_xlabel('Atomic distortion ($\mathrm{\AA}$)', fontsize=18)
#ax1.set_ylabel('Count')
ax1.set_title('(b) Distortion', fontsize=22)
ax1.tick_params(axis='x', colors='r')
ax1.xaxis.label.set_color('r')


#===============================================
de = df['de']
print(len(de), max(de), min(de))
de = de[de<0.5]
de = de[de>-0.5]
print(len(de), max(de), min(de))
n, bins, patches = ax3.hist(de*1000, 50, density=False, color='b')
ax3.set_xlabel('$\Delta$E (meV/atom)', fontsize=18)
ax3.set_title('(c) Energy difference', fontsize=22)
ax3.tick_params(axis='x', colors='b')
ax3.xaxis.label.set_color('b')


#ax2 = fig.add_subplot(212)
count = 0
data = np.zeros([32, 32])
for spg1, spg2 in zip(df['spg1'], df['spg2']):
    pg1 = Group(spg1, quick=True).pg_number
    pg2 = Group(spg2, quick=True).pg_number
    data[pg1-1, pg2-1] += 1
    #print(count, pg1, pg2)
    count += 1

for i in range(32):
    for j in range(32):
        if data[i, j] > 0:
            ax2.plot([i, j], [0,1], '-k', lw=0.01*data[i,j])
            print(i, j, data[i, j])

ax2.grid(False)
ax2.set_xlim(-0.5, 31)
ax2.set_ylim(0, 1)
ax2.set_yticks([])
ax2.set_xticks([])

secax = ax2.secondary_xaxis('top')
secax.tick_params(axis='x', colors='b')
#secax = ax2.twiny()
secax.set_xticks(range(32))
secax.set_xticklabels(['1', '$\overline{1}$', '2', '$m$', '$2/m$', '222', '$mm2$', '$mmm$', 
                    '4', '$\overline{4}$', '$4/m$', '422', '$4mm$', '$\overline{4}2m$', '$4/mmm$', 
                    '3', '$\overline{3}$', '32', '$3m$', '$\overline{3}m$', 
                    '6', '$\overline{6}$', '6/m', '622', '6mm', '$\overline{6}$2m', '6/mmm', 
                    '23', '$m\overline{3}$', '432', '$\overline{4}3m$', '$m\overline{3}m$'],
                    rotation = 45, fontsize=18)

secax.set_xlabel('(d) Point group relation', fontsize=22)
#secax.xaxis.label.set_color('b')

becax = ax2.secondary_xaxis('bottom')
becax.set_xticks(range(32))
becax.set_xticklabels(['1', '$\overline{1}$', '2', '$m$', '$2/m$', '222', '$mm2$', '$mmm$', 
                    '4', '$\overline{4}$', '$4/m$', '422', '$4mm$', '$\overline{4}2m$', '$4/mmm$', 
                    '3', '$\overline{3}$', '32', '$3m$', '$\overline{3}m$', 
                    '6', '$\overline{6}$', '6/$m$', '622', '6$mm$', '$\overline{6}$2m', '6/$mmm$', 
                    '23', '$m\overline{3}$', '432', '$\overline{4}3m$', '$m\overline{3}m$'],
                    rotation = 45, fontsize=18)

becax.tick_params(axis='x', colors='c')
becax.xaxis.label.set_color('c')
#becax.set_xlabel('Low symmetry', fontsize=20)

#=============================Pie
recipe = ["20 Elemental red",
          "934 Binary yellow",
          "2078 Ternary black",
          "1382 Quaternary blue",
          "100 Pentanary orange",
          ]

data = [int(x.split()[0]) for x in recipe]
names = [x.split()[1] for x in recipe]
colors = [x.split()[-1] for x in recipe]

N = len(df['spg1'])
x = np.arange(len(data))
width = 0.5
rects = axs.bar(x, data, width, color=colors, log=True)
axs.set_ylim(0, 8000)
axs.set_ylabel('Count', fontsize=18)
axs.set_xticks(x)
axs.set_xticklabels(names, rotation=60, fontsize=18)

for rect in rects:
    height = rect.get_height()
    axs.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
axs.set_title("(a) Stoichiometry", fontsize=22)
axs.grid(False)


plt.tight_layout()
plt.savefig('Fig3-stat.pdf')

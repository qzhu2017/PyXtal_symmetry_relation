# Group-subgroup symmetry relation applied to phase transition

This is a public repository to explain the work in [Symmetry Relation Database and Its Application to Ferroelectric Materials Discovery, Zhu, et al, 2022](https://arxiv.org/abs/2208.10655)

## Dataset (in ase.database format)
- `All_mp_2022.db`: all identified structure pairs in by [Zhu, et al](https://arxiv.org/abs/2208.10655)
- `Smidt_2020.db`: all identified structure pairs in by [Smidt, et al](https://www.nature.com/articles/s41597-020-0407-9)

Both files are constructed based on the [ASE.database format](https://wiki.fysik.dtu.dk/ase/ase/db/db.html)

One can access the data by referring to the above documentation. 
Command mode is also possible as follows
```
$ ase db dataset/All_mp_2022.db 
id|age|user|formula  |natoms|pbc| volume|charge|    mass
 1|17M|qzhu|Pb2S2    |     4|TTT|113.951| 0.000| 478.520
 2|17M|qzhu|Pb2S2    |     4|TTT|110.514| 0.000| 478.520
 3|17M|qzhu|Nd2Pd2As2|     6|TTT|130.635| 0.000| 651.167
 4|17M|qzhu|Nd2Pd2As2|     6|TTT|130.898| 0.000| 651.167
 5|17M|qzhu|Ca2Hg2Sn2|     6|TTT|162.916| 0.000| 718.760
 6|17M|qzhu|Ca2Hg2Sn2|     6|TTT|165.999| 0.000| 718.760
 7|17M|qzhu|Pd2Pr2Sb2|     6|TTT|148.763| 0.000| 738.175
 8|17M|qzhu|Pd2Pr2Sb2|     6|TTT|150.570| 0.000| 738.175
 9|17M|qzhu|Cu2Ga2U2 |     6|TTT|105.859| 0.000| 742.596
10|17M|qzhu|Cu2Ga2U2 |     6|TTT|105.555| 0.000| 742.596
11|17M|qzhu|Ca2Pb2Zn2|     6|TTT|154.206| 0.000| 625.316
12|17M|qzhu|Ca2Pb2Zn2|     6|TTT|157.389| 0.000| 625.316
13|17M|qzhu|Au2Ce2Sn2|     6|TTT|152.525| 0.000| 911.585
14|17M|qzhu|Au2Ce2Sn2|     6|TTT|152.029| 0.000| 911.585
15|17M|qzhu|Ba2V12O22|    36|TTT|414.155| 0.000|1237.930
16|17M|qzhu|Ba2V12O22|    36|TTT|414.309| 0.000|1237.930
17|17M|qzhu|Pd2Tb2Sb2|     6|TTT|136.580| 0.000| 774.211
18|17M|qzhu|Pd2Tb2Sb2|     6|TTT|138.986| 0.000| 774.211
19|17M|qzhu|Pd2Sm2Sb2|     6|TTT|142.093| 0.000| 757.080
20|17M|qzhu|Pd2Sm2Sb2|     6|TTT|143.647| 0.000| 757.080
Rows: 4558 (showing first 20)
Keys: dE, gap, max_disp, mpr_id, name, path, space_group, status, time_cost, type
```

## Tutorial
- [Demo.ipynb](https://nbviewer.org/github/qzhu2017/PyXtal_symmetry_relation/blob/main/Demo.ipynb): a tutorial to explain the concepts of symmetry relation and the relevant tools in PyXtal for the automated analysis of symmetry relation. 

To run the tutorial, it is required to to install [PyXtal](https://github.com/qzhu2017/PyXtal) via `pip install pyxtal`.

## Figures
The related scripts to plot the figures in [Zhu, et al](https://arxiv.org/abs/2208.10655).

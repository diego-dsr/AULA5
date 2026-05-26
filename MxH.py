import sys
sys.path.append(r'C:\Users\diego\OneDrive\Documentos\GitHub\AULA5')
import magdynlab.utils.MxH_A
medida_MxH = magdynlab.utils.MxH_A.MxH
import sys
#import magdynlab.utils.MxH_A
#medida_MxH = magdynlab.utils.MxH_A.MxH
#import magdynlab.utils.nVxH
#ISHE = magdynlab.utils.nVxH.nVxH
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Leitura das medidas
R23  = MxH(r'C:\Users\diego\OneDrive\Documentos\GitHub\AULA5\R23_002')
R23A = MxH(r'C:\Users\diego\OneDrive\Documentos\GitHub\AULA5\R23A_001')
R23B = MxH(r'C:\Users\diego\OneDrive\Documentos\GitHub\AULA5\R23B_002')
R23C = MxH(r'C:\Users\diego\OneDrive\Documentos\GitHub\AULA5\R23C_002')

# Cria a figura
plt.figure('MxH', figsize=(5, 4))

# Plota e guarda os "handles" de cada curva
h1 = R23.plotMn('ko-', 'MxH')
h2 = R23A.plotMn('ro-', 'MxH')
h3 = R23B.plotMn('bo-', 'MxH')
h4 = R23C.plotMn('go-', 'MxH')

# Adiciona legenda manualmente
plt.legend(['N = 1', 'N = 2', 'N = 3', 'N = 4'], loc='best')

# Ajustes do gráfico
plt.xlim(-60, 20)
plt.ylim(-1.3, 1.3)
plt.xlabel('H (Oe)')
plt.ylabel('$M/M_s$ (a.u.)')
plt.title(f'$[NiFe/IrMn/Ta]_N$')
plt.grid(True)
plt.tight_layout()
#plt.savefig(f'/home/saldanha/UFSM/Ricardo/MxH/R23/R23_A_B_C.png', dpi=150, bbox_inches='tight')

plt.show()
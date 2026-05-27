import sys

print(sys.executable)
print(sys.version)

import numpy
print(numpy.__version__)
sys.path.append(r'C:\Users\diego\OneDrive\Documentos\GitHub\AULA5')
import MxH_A
medida_MxH = MxH_A.MxH
import sys
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

# Leitura das medidas
R23  = medida_MxH(r'C:\Users\diego.saldanha\Documents\AULA\AULA5\R23_002')
R23A = medida_MxH(r'C:\Users\diego.saldanha\Documents\AULA\AULA5\R23A_001')
R23B = medida_MxH(r'C:\Users\diego.saldanha\Documents\AULA\AULA5\R23B_002')
R23C = medida_MxH(r'C:\Users\diego.saldanha\Documents\AULA\AULA5\R23C_002')

# Cria a figura
plt.figure('MxH', figsize=(8,6))

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
#plt.savefig(f'C:\Users\diego.saldanha\Documents\AULA\AULA5\R23_A_B_C.png', dpi=150, bbox_inches='tight')

plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:51:49 2022

@author: DISRCT
"""

# import numpy as np
import matplotlib.pyplot as plt
# import math




cidade = ["Araucária", "Campo Largo", "Colombo", "Fazenda Rio Grande", "Pinhais", "São José dos Pinhais"]
val = [141410, 130091, 240840, 98368, 130789, 317476]

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d} Hab'.format(p=pct,v=val)
    return my_autopct

plt.figure(figsize=(6,6))
plt.pie(val, labels=cidade, autopct=make_autopct(val))
plt.savefig('Atividade 2.png')
plt.show()
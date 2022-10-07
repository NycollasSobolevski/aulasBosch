# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 09:00:32 2022

@author: DISRCT
"""

import math

num = int(input('Insira um valor maior que zero: '))

x = [(num//(10**i))%10 for i in range(math.ceil(math.log(num, 10))-1, -1, -1)]

print(x)
print(f'A soma dos algarismos é igual a {sum(x)}')

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:51:15 2022

@author: disrct
"""

times = ['1_palmeiras','2_coritiba','1_corinthians','3_juventude','2_fluminense','3_bahia','1_cuiaba','3_ponte preta','2_parana clube','3_voltaredonda']

times = sorted(times)
divisaoUm = times[:3]
divisaoDois = times[3:6]
divisaoTres = times[6:]
for i in range(len(divisaoUm)):
    divisaoUm[i] = divisaoUm[i].replace("1_","")
for i in range(len(divisaoDois)):
    divisaoDois[i] = divisaoDois[i].replace("2_","")
for i in range(len(divisaoTres)):
    divisaoTres[i] = divisaoTres[i].replace("3_","")

    

print ("\n\nDivisão um:",divisaoUm)
print ("\n\nDivisão dois:",divisaoDois)
print ("\n\nDivisão tres:",divisaoTres)

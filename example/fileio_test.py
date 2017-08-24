#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
with open("salary.txt", 'r') as f:
    lines = f.readlines()

sal_re = r"([a-zA-Z0-9,]+만원)"
tot_sal = 0
sal_cnt = 0
exp_re = r"[0-9.]+%"
tot_exp = 0
exp_cnt = 0
for idx, line in enumerate(lines):
    sal = (re.search(sal_re, line).group()).replace('만원','').replace(',','')
    if len(sal) > 0:
        tot_sal += int(sal)
        sal_cnt += 1
    exp = (re.search(exp_re, line).group()).replace('%','')
    if len(exp) > 0:
        tot_exp += float(exp)
        exp_cnt += 1
    print (line, sal, exp)

print(len(lines), tot_sal, sal_cnt, tot_exp, exp_cnt)
print('avg_sal = ', float(tot_sal)/sal_cnt)        
print('avg_exp = ', (tot_exp)/exp_cnt)

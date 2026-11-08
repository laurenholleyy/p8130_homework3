# Question 7
import numpy as np
from scipy.stats import t

n1, m1, s1 = 8, 14, 4
n2, m2, s2 = 20, 11, 2

## Part A
v1, v2 = s1**2/n1, s2**2/n2
se_w = np.sqrt(v1 + v2)
df_w = (v1 + v2)**2/(v1**2/(n1-1)+v2**2/(n2-1))
stat_w = (m1 - m2)/se_w
p_w = 2*t.sf(abs(stat_w), df_w)
diff = m1 - m2
ci = diff + np.array([-1,1])*t.ppf(0.975, df_w)*se_w
print(diff)
print(se_w)
print(stat_w)
print(df_w)
print(p_w)
print(ci)

## Part B
df_p = n1 + n2 - 2
sp2 = ((n1 - 1)*s1**2+(n2-1)*s2**2)/df_p
se_p = np.sqrt(sp2*(1/n1+1/n2))
stat_p = (m1 - m2)/se_p
p_p = 2*t.sf(abs(stat_p), df_p)
print(sp2)
print(se_p)
print(stat_p)
print(df_p)
print(p_p)
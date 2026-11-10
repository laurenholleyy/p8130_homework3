# Question 9
import numpy as np
from scipy.stats import norm, chi2_contingency

## Part A

p1, p2 = 36/120, 60/150
d = p1 - p2
se = (((p1*(1-p1))/120) + ((p2*(1-p2))/150))**0.5
lo, hi = d-norm.ppf(0.975)*se, \
    d + norm.ppf(0.975)*se
    
print(f"p1 = {p1:.4f}, p2 = {p2:.4f}")
print(f"Difference = {d:.4f}")
print(f"SE = {se:.5f}")
print(f"CI = [{lo:.4f}, {hi:.4f}]")

## Part B

x1, x2, n1, n2 = 36, 60, 120, 150
pp = (x1 + x2)/(n1 + n2)
se0 = (pp*(1-pp)*(1/n1 + 1/n2))**0.5
z = (p1 - p2)/se0
pv = 2*norm.sf(abs(z))

print(f"Pooled p = {pp:.4f}")
print(f"Null SE = {se0:.5f}")
print(f"z = {z:.4f}")
print(f"p = {pv:.8f}")

## Part C

tab = np.array([[36, 84], [60, 90]])
q, pchi, df, e = chi2_contingency(tab, correction = False)

print(f"Q = {q:.4f}; df = {df}")
print(f"p = {pchi:.8f}")
print("Expected counts:")
print(e)
print(f"z^2 = {z*z:.4f}")
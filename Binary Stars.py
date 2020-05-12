import pandas as pd
import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt
c= 3*(10**8)
pie= 3.141592653589793238
G= 6.67408*(10**(-11))
df =pd.read_csv('assignment.csv')
df['v1']=df.redshift1 * c
df['v2']=df.redshift2 *c

from scipy import optimize

def test_func(x, a, b,c):
    return a * np.sin(b * x)+c

params, params_covariance = optimize.curve_fit(test_func, df.time, df.v2,
                                               p0=[15000, 1.57079632679, 25000])
print(params)

plt.figure(figsize=(30, 20))
plt.title('star')
plt.scatter(df.time,df.v1,label='star1',s=50)
plt.scatter(df.time,df.v2,label='star2',s=50)
plt.plot(df.time, test_func(df.time, params[0], params[1], params[2]), color='black', label='sine function')
plt.xlabel('Time')
plt.ylabel('Orbital Velocity')
plt.legend()
plt.show

v1max= df.v1.max()
v2max= df.v2.max()
i1=0
i2=0
for i in range (1000):
    if (df.v2[i]==v2max):
        i1=i
    if (df.v1[i]==v1max):
        i2=i
        break
T= (df.time[i2]-df.time[i1])*2
vradial= v1max-v2max
if(vradial<0):
    vradial = vradial*(-1)
m1 = (((T**2)*(v2max**3)*((v1max+v2max)**3))/((2*(np.pi)*G)**2))
m2 = (((T**2)*(v1max**3)*((v1max+v2max)**3))/((2*(np.pi)*G)**2))

mh= max(m1, m2)
ml = min(m1, m2)
print ("Period of revolution is:", T)
print ("Mass of lighter star is:", ml)
print ("Mass of heavier star is:", mh)


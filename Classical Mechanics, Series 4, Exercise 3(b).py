import numpy as np
import matplotlib.pyplot as plt
import math
import time

# --- Timer for Benchmark ---

start_time = time.time()

# Numerical Integration using leapfrog method
# Initial conditions:
#   theta(0) = theta_0 = 3/4 * pi
#   theta_dot(0) = 0

N = 100000
t = np.linspace(0,300,N)
dt = t[1] - t[0]
g = -9.81
l = 1

# --------- Initialisation of variables ----------
theta = np.zeros(N)
theta[0] = 3/4 * math.pi
theta_dot = np.zeros(N)
theta_dot[0] = 0
a = np.zeros(N)
a[0] = -g/l * math.sin(theta[0])

# --------- Integration --------
for i in range(N-1):
    theta[i+1] = theta[i] + theta_dot[i]*dt + 1/2 * a[i] * dt**2
    a[i+1] = -g/l * math.sin(theta[i+1])
    theta_dot[i+1] = theta_dot[i] + 1/2 *(a[i] + a[i+1])*dt

print("--- % seconds ---" % (time.time()-start_time))

plt.plot(theta,theta_dot)
plt.xlabel('Theta')
plt.ylabel('Theta Dot')
plt.title('Classical Mechanics Series 4, Exercise 3(b): Phase Space')
plt.show()
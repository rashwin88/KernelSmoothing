from kernel_smoothing.base_functions import quadratic_mid_line_sine_wave as qsw
from kernel_smoothing.base_functions import logistic_curve as lsw
from kernel_smoothing.helpers import create_normal_perturbations as cnp
import matplotlib.pyplot as plt
a = qsw.quadratic_midline_sine_wave(B=4,interval_length=0.01)
a.append(cnp.create_normal_perturbations(a[1], variance=6))
plt.plot(a[0], a[1])
plt.scatter(a[0], a[2], alpha=0.2)
plt.show()


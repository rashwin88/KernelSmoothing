from kernel_smoothing.base_functions import quadratic_mid_line_sine_wave as qsw
from kernel_smoothing.base_functions import logistic_curve as lsw
from kernel_smoothing.helpers import create_normal_perturbations as cnp

from kernel_smoothing.core_functions import compute_nadarya_watson_wa as cnwa
import matplotlib.pyplot as plt


a = qsw.quadratic_midline_sine_wave(B=4,interval_length=0.01)
a.append(cnp.create_normal_perturbations(a[1], variance=6))

# we have the normal perturbations
training_points = [a[0], a[2]]
a.append(
    [cnwa.compute_nadarya_watson_wa(x, training_points, 0.1) for x in a[0]]
)
a.append(
    [cnwa.compute_nadarya_watson_wa(x, training_points, 0.5) for x in a[0]]
)
a.append(
    [cnwa.compute_nadarya_watson_wa(x, training_points, 1) for x in a[0]]
)
a.append(
    [cnwa.compute_nadarya_watson_wa(x, training_points, 1.5) for x in a[0]]
)

plt.scatter(a[0], a[2], alpha=0.3)
plt.plot(a[0], a[1], color = 'red')
plt.plot(a[0], a[3], color = 'blue')
plt.plot(a[0], a[4], color = 'blue')
plt.plot(a[0], a[5], color = 'blue')
plt.show()


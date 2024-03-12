import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import linalg
from scipy.optimize import minimize
import seaborn as sns


flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e",
                  "#2ecc71"]
sns.set_palette(sns.color_palette(flatui))
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (7, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
plt.rcParams.update(params)


def squares(x):

    weeks = 1 * 52
    t = np.arange(1, weeks + 1, 1)
    data = [2.196,2.228,0.692,1.862,1.444,2.351,4.903,5.264,4.264,3.547,6.731,10.447,7.909,4.949,3.299,3.246,2.216,1.99,2.287,1.772,1.283,1.21,1.84,1.76,2.853,0.708]
    data2 = [0.869,0.946,0.722,0.774,0.892,0.925,0.808,0.745,0.668,0.675,0.716,1.132,1.33,0.623,0.674,0.608,0.533,0.6,0.467,0.279,0.416,0.297,0.207,0.221,0.282,0.236,0.255,
             0.231,0.229,0.263,0.177,0.15,0.126,0.093,0.068,0.047,0.048,0.086,0.092,0.107,0.172,0.291,0.514,0.917,0.903,0.792,0.768,0.818,0.954,1.008,0.712,0.961]

    reg = sum((x[0]*np.sin(0.1208*t[i]+x[1])+ x[2] - data2[i])**2 for i in range(len(t)))


    return reg


def inv_2(t, y, w): #weighted regression minimization

    reg = sum(w[i] * (t[i] - y[i]) ** 2 for i in range(len(t)))

    return reg


def tss(t, y, w): #R-squared calculation
    meanY = sum(w[i] * y[i] for i in range(len(t)))
    return sum(w[i] * (meanY - y[i]) ** 2 for i in range(len(t)))

def main():

    """jac = np.array([[8.85116476e+00, 9.32942640e+08, 3.89012864e+01, 1.02315263e+01]])
    hess = np.matmul(jac.T,jac)
    print(hess)
    print(linalg.det(hess))
    hess2 = np.diag(hess)*np.identity(4)
    cov = linalg.inv(hess2)
    print(cov)
    scale = 1/np.average([0.01,0.04,0.46,0,0.12,0.08,0.16,0.08,0.18,0.11,0.57,0.51,0.42,0.53,1,0.41,0.06,0.09,0.24,0.11,0.18,0.32,0.12,0.17,0.07,0.02])
    chi2dof = scale*61.59 / (26 - 4)
    cov *= chi2dof
    perr = np.sqrt(np.diag(cov))
    print(perr)"""

    x0 = np.array([0.5, 0.0, 0.5])  # initial guess for curve fit parameters
    # weighted least squares nonlinear regression with bounds
    result = minimize(squares, x0, method='BFGS',
                   bounds=((None, None), (None, None), (None, None)), tol=1e-6)
    print(result)
      # give parameters a variable name

    """jac = np.array([result.jac])
    hess = np.matmul(jac.T, jac)
    hess2 = np.diag(hess) * np.identity(3)
    cov = linalg.inv(hess2)"""
    cov = result.hess_inv

    chi2dof = result.fun / (52 - 3)
    cov *= chi2dof
    variance = np.diag(cov)
    print(result.x)
    print(variance)

    model = [1.40660044,1.3272771,1.25045585,1.18178664,1.12453079,1.0800861,1.04865973,1.02981894,1.02285358,1.0269792,1.04143064,1.0654871,
             1.09845408,1.13961335,1.18814224,1.24299604,1.30274466,1.36535858,1.42795683,1.48657396,1.53608115,1.57049558,1.58393885,1.57228308,
             1.53495746,1.47584179]
    cystData = [1.58, 2.15, 0.52, 3, 1.87, 2.33, 1.32, 1.92, 2.62, 2.35, 0.14, 0.83, 1.12, 1.42, 1.02, 1.36, 1.75, 1.74,
                1.01, 1.51, 1.2, 1.43, 2.74, 2.03, 1.27, 1.56]
    weights = [0.01, 0.04, 0.46, 0, 0.12, 0.08, 0.16, 0.08, 0.18, 0.11, 0.57, 0.51, 0.42, 0.53, 1, 0.41, 0.06, 0.09,
               0.24, 0.11, 0.18, 0.32, 0.12, 0.17, 0.07, 0.02]
    weights = list(np.array(weights)/sum(weights))
    print(weights)

    rsquare = 1 - inv_2(model, cystData, weights) / tss(model, cystData,weights)  # R-square calculation, see tss
    print('r-square = ' + str(rsquare))




main()
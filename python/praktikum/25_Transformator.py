from numpy import abs, append, array, linspace, ones, sqrt
from numpy.typing import NDArray
from tools.python.plot import DefaultScatter
from tools.statistics.linear_regression import linreg, plotWithErrorBars, scatterWithErrorBars
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

import matplotlib.pyplot as plt

# Units: U in V, I in A, R in Ohm
U_uncertainty = 0.01
I_uncertainty = 1e-5
X = linspace(1, 10, 1000)

def PlotInductivitiesAndKappa(loop_ratio, L1, L1_uncertainty, L2, L2_uncertainty, L12, L12_uncertainty, kappa, kappa_uncertainty):
    _, axs = plt.subplots(2, 1)

    scatterWithErrorBars(axs[0], loop_ratio, L1[0:11], y_absErr=L1_uncertainty[0:11], scatter_label=r'$L_1$', fmt='r.')
    scatterWithErrorBars(axs[0], loop_ratio, L2[0:11], y_absErr=L2_uncertainty[0:11], scatter_label=r'$L_2$', fmt='g.')
    scatterWithErrorBars(axs[0], loop_ratio, L12[0:11], y_absErr=L12_uncertainty[0:11], scatter_label=r'$L_{12}$', ylabel="L [T]", fmt='b.')
    ax = axs[0].twinx()
    ax.yaxis.set_label_position("right")
    scatterWithErrorBars(ax, loop_ratio, kappa[0:11], y_absErr=kappa_uncertainty[0:11], title=r'Experimentell bestimmte Induktivtäten und Kopplungsgrad bei $130 Hz$', scatter_label=r'Kopplungsgrad $\kappa$',
                         xlabel=r'$N_2 / N_1$', ylabel=r'Kopplungsgrad $\kappa$', fmt='k.', legend_loc='right', grid=False)
    
    scatterWithErrorBars(axs[1], loop_ratio, L1[11:22], y_absErr=L1_uncertainty[11:22], scatter_label=r'$L_1$', fmt='r.')
    scatterWithErrorBars(axs[1], loop_ratio, L2[11:22], y_absErr=L2_uncertainty[11:22], scatter_label=r'$L_2$', fmt='g.')
    scatterWithErrorBars(axs[1], loop_ratio, L12[11:22], y_absErr=L12_uncertainty[11:22], scatter_label=r'$L_{12}$', ylabel="L [T]", fmt='b.')
    ax = axs[1].twinx()
    ax.yaxis.set_label_position("right")
    scatterWithErrorBars(ax, loop_ratio, kappa[11:22], y_absErr=kappa_uncertainty[11:22], title=r'Experimentell bestimmte Induktivtäten und Kopplungsgrad bei $320 Hz$', scatter_label=r'Kopplungsgrad $\kappa$',
                         xlabel=r'$N_2 / N_1$', ylabel=r'Kopplungsgrad $\kappa$', fmt='k.', legend_loc='right', grid=False)
    
    #DefaultScatter(axs[0], loop_ratio, L1[0:11], label=r'$L_1$', c="r")
    #DefaultScatter(axs[0], loop_ratio, L2[0:11], label=r'$L_2$', c="g")
    #DefaultScatter(axs[0], loop_ratio, L12[0:11], label=r'$L_{12}$', c="b")
    #DefaultScatter(axs[0], loop_ratio, kappa[0:11], title=r'Experimentell bestimmte Induktivtäten und Kopplungsgrad bei $130 Hz$', label=r'Kopplungsgrad $\kappa$',
    #                xlabel=r'$N_2 / N_1$')
    #DefaultScatter(axs[1], loop_ratio, L1[11:22], label=r'$L_1$', c="r")
    #DefaultScatter(axs[1], loop_ratio, L2[11:22], label=r'$L_2$', c="g")
    #DefaultScatter(axs[1], loop_ratio, L12[11:22], label=r'$L_{12}$', c="b")
    #DefaultScatter(axs[1], loop_ratio, kappa[11:22], title=r'Experimentell bestimmte Induktivtäten und Kopplungsgrad bei $320 Hz$', label=r'Kopplungsgrad $\kappa$',
    #                xlabel=r'$N_2 / N_1$')
    
    plt.tight_layout()
    #plt.show()


def UfromI(I: NDArray, R:NDArray):
    return R*I

def Ratio(var1: NDArray, var2: NDArray) -> NDArray:
    return var2/var1

def PlotRatios(ax, var1: NDArray, var2: NDArray, other_ratio: NDArray, uncertainty=0, title="", xlabel="", ylabel=""):
    ratio, funcertainty = GetResultAndUncertainty(Ratio, [var1, var2], True, [uncertainty, uncertainty])
    fun, _, _ = linreg(other_ratio, ratio)
    plotWithErrorBars(ax, other_ratio, ratio, fun, y_absErr=funcertainty,
                      title=title, fun_label="Lineare Regression",
                      scatter_label="Messwerte mit Unsicherheit", xlabel=xlabel, ylabel=ylabel)
    
def kappa_fun(L1: NDArray, L2: NDArray, L12: NDArray) -> NDArray:
    return L12 / sqrt(abs(L1*L2))

N1 = 50
N2 = array([85, 100, 120, 140, 170, 200, 240, 290, 350, 420, 500])
N = N2.size
loop_ratio = N2/N1

def Exp1():
    def plot(ax, U1, U2, omega):
        ax.plot(X, X, '--g', label="Theoriekurve")
        PlotRatios(ax, U1, U2, loop_ratio, uncertainty=U_uncertainty,
               title=r'Spannungs- und Windungsverhältnis im offenen Betrieb für $%.f Hz$' % omega, xlabel=r'$N_2 / N_1$', ylabel=r'$U_2 / U_1$')
        ax.legend()

    def LfromU(U1: NDArray, I1: NDArray, omega: float):
        return U1 / (omega * I1)
    
    _, axs = plt.subplots(2,1)

    omega = 130
    U1 = 0.28 * ones(N)
    I1 = 0.04 * ones(N)
    U2 = array([0.35 ,0.41 ,0.49 ,0.57 ,0.69 ,0.82 ,0.98 ,1.18 ,1.43, 1.71, 2.04])
    L1_full, L1_uncertainty_full = GetResultAndUncertainty(LfromU, [U1, I1, omega*ones(N)], True, [U_uncertainty, I_uncertainty, 0])
    L12_full, L12_uncertainty_full = GetResultAndUncertainty(LfromU, [U2, I1, omega*ones(N)], True, [U_uncertainty, I_uncertainty, 0])
    plot(axs[0], U1, U2, omega)

    omega = 320
    U1 = 0.59 * ones(N)
    I1 = 0.03 * ones(N)
    U2 = array([0.75, 0.87, 1.05, 1.23, 1.5, 1.76, 2.12, 2.57, 3.1, 3.73, 4.44])
    L1, L1_uncertainty =GetResultAndUncertainty(LfromU, [U1, I1, omega*ones(N)], True, [U_uncertainty, I_uncertainty, 0])
    L1_full = append(L1_full, L1)
    L1_uncertainty_full = append(L1_uncertainty_full, L1_uncertainty)
    L12, L12_uncertainty = GetResultAndUncertainty(LfromU, [U2, I1, omega*ones(N)], True, [U_uncertainty, I_uncertainty, 0])
    L12_full = append(L12_full, L12)
    L12_uncertainty_full = append(L12_uncertainty_full, L12_uncertainty)
    plot(axs[1], U1, U2, omega)
    
    plt.tight_layout()
    #plt.show()

    return L1_full, L1_uncertainty_full, L12_full, L12_uncertainty_full

def Exp2(L12: NDArray, L12_uncertainty: NDArray):    
    def plot(ax, I1, I2, omega):
        ax.plot(X, X, '--g', label="Theoriekurve")
        PlotRatios(ax, I2, I1, loop_ratio, uncertainty=I_uncertainty,
               title=r'Stromstärke- und Windungsverhältnis im Kurzschlussetrieb für $%.f Hz$' % omega, xlabel=r'$N_2 / N_1$', ylabel=r'$I_1 / I_2$')
        ax.legend()

    def L2fromL12(L12: NDArray, current_ratio: NDArray):
        return L12 * current_ratio
    
    _, axs = plt.subplots(2,1)

    omega = 130
    U1 = array([0.21, 0.18, 0.145, 0.12, 0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.043])
    I1 = 0.05 * ones(N)
    I2 = array([19.26, 18.475, 17.05, 15.575, 13.56, 11.895, 10.165, 8.56, 7.16, 6, 5.06])*10**(-3)
    current_ratio = I1/I2
    plot(axs[0], I1, I2, omega)

    omega = 320
    U1 = array([96, 82, 69, 61, 53, 48, 44, 41, 39, 37, 36])*10**(-3)
    I1 = 0.04 * ones(N)
    I2 = array([28, 24.3, 20.5, 17.7, 14.6, 12.4, 10.3, 8.5, 7, 5.8, 4.9])*10**(-3)
    current_ratio = append(current_ratio, I1/I2)
    L2, L2_uncertainty = GetResultAndUncertainty(L2fromL12, [L12, current_ratio], True, [L12_uncertainty, 0])
    plot(axs[1], I1, I2, omega)
    
    plt.tight_layout()
    #plt.show()

    return L2, L2_uncertainty

def Exp3(R_coil1: float, R_coil2: NDArray):
    def plot(ax, U1, U2, omega, R):
        ax.plot(X, X, '--g', label="Theoriekurve bei idealer Kopplung")
        PlotRatios(ax, U1, U2, loop_ratio, uncertainty=U2_uncertainty,
               title=r'Spannungs- und Windungsverhältnis unter Belastung für $%.f Hz$ und $%.f \Omega$ Last' % (omega, R), xlabel=r'$N_2 / N_1$', ylabel=r'$U_2 / U_1$')
        ax.legend()
        
    def plot_corr(ax, U1, U2, omega, R):
        ax.plot(X, X, '--g', label="Theoriekurve bei idealer Kopplung")
        PlotRatios(ax, U1, U2, loop_ratio, uncertainty=U2_uncertainty,
               title=r'Korrigiertes Spannungs- und Windungsverhältnis unter Belastung für $%.f Hz$ und $%.f \Omega$ Last' % (omega, R), xlabel=r'$N_2 / N_1$', ylabel=r'$U_2 / U_1$')
        ax.legend()

    def U1Correction(omega: float, U1: NDArray, R_coil: float, R_load: float, L1: NDArray, L2: NDArray) -> NDArray:
        denominator_fraction = (1j*omega*L2 + R_load) / (1j*omega*L1*R_load)
        denominator = abs(1 + R_coil * denominator_fraction)
        return U1 / denominator

    _, axs = plt.subplots(2,2)

    R = 100
    omega = 130
    U1 = array([375, 366.5, 352, 335, 307, 278, 241, 201, 164, 133, 108])*10**(-3)
    I1 = 0.05 * ones(N)
    I2 = array([3.86, 4.36, 4.985, 5.48, 5.99, 6.24, 6.315, 6.12, 5.69, 5.145, 4.57])*10**(-3)
    U2, U2_uncertainty = GetResultAndUncertainty(UfromI, [I2, ones(N)*R], True, [I_uncertainty, 0])
    #plot(axs[0][0], U1, U2, omega, R)
    U1_corr, U1_corr_uncertainty = GetResultAndUncertainty(U1Correction, [omega*ones(N), U1, R_coil1*ones(N), R*ones(N), L1[0:11], L2[0:11]], True, [0, U_uncertainty, 0, 0, 0, 0]) # TODO: Coil and resistance uncertainty
    U2_corr, U2_corr_uncertainty = GetResultAndUncertainty(UfromI, [I2, R_coil2+R], True, [I_uncertainty, 0])
    plot_corr(axs[0][0], U1_corr, U2_corr, omega, R)

    omega = 320
    U1 = array([678, 634, 570, 507.5, 424, 355, 284, 220, 170, 132, 105])*10**(-3)
    I1 = 0.04e-3 * ones(N)
    I2 = array([7.5, 8.15, 8.7, 9, 8.95, 8.6, 8, 7.2, 6.3, 5.4, 4.65])*10**(-3)
    U2, U2_uncertainty = GetResultAndUncertainty(UfromI, [I2, ones(N)*R], True, [I_uncertainty, 0])
    #plot(axs[1][0], U1, U2, omega, R)
    U1_corr, U1_corr_uncertainty = GetResultAndUncertainty(U1Correction, [omega*ones(N), U1, R_coil1*ones(N), R*ones(N), L1[11:22], L2[11:22]], True, [0, U_uncertainty, 0, 0, 0, 0]) # TODO: Coil and resistance uncertainty
    U2_corr, U2_corr_uncertainty = GetResultAndUncertainty(UfromI, [I2, R_coil2+R], True, [I_uncertainty, 0])
    plot_corr(axs[1][0], U1_corr, U2_corr, omega, R)

    R = 3000
    omega = 130
    U1 = array([395, 394.5, 394, 394, 393, 392, 390.5, 388, 384, 378, 369])*10**(-3)
    I1 = 0.05 * ones(N)
    I2 = array([0.15, 0.18, 0.21, 0.25, 0.3, 0.35, 0.42, 0.5, 0.59, 0.7, 0.81])*10**(-3)
    U2, U2_uncertainty = GetResultAndUncertainty(UfromI, [I2, ones(N)*R], True, [I_uncertainty, 0])
    #plot(axs[0][1], U1, U2, omega, R)
    U1_corr, U1_corr_uncertainty = GetResultAndUncertainty(U1Correction, [omega*ones(N), U1, R_coil1*ones(N), R*ones(N), L1[0:11], L2[0:11]], True, [0, U_uncertainty, 0, 0, 0, 0]) # TODO: Coil and resistance uncertainty
    U2_corr, U2_corr_uncertainty = GetResultAndUncertainty(UfromI, [I2, R_coil2+R], True, [I_uncertainty, 0])
    plot_corr(axs[0][1], U1_corr, U2_corr, omega, R)

    omega = 320
    U1 = array([833, 831.5, 828.5, 825, 818, 810, 797, 777.5, 750, 713, 667])*10**(-3)
    I1 = 0.04 * ones(N)
    I2 = array([0.31, 0.36, 0.43, 0.5, 0.61, 0.71, 0.84, 0.99, 1.16, 1.32, 1.46])*10**(-3)
    U2, U2_uncertainty = GetResultAndUncertainty(UfromI, [I2, ones(N)*R], True, [I_uncertainty, 0])
    #plot(axs[1][1], U1, U2, omega, R)
    U1_corr, U1_corr_uncertainty = GetResultAndUncertainty(U1Correction, [omega*ones(N), U1, R_coil1*ones(N), R*ones(N), L1[11:22], L2[11:22]], True, [0, U_uncertainty, 0, 0, 0, 0]) # TODO: Coil and resistance uncertainty
    U2_corr, U2_corr_uncertainty = GetResultAndUncertainty(UfromI, [I2, R_coil2+R], True, [I_uncertainty, 0])
    plot_corr(axs[1][1], U1_corr, U2_corr, omega, R)
        
    plt.tight_layout()
    plt.show()

### 3.4
f = 500 #Hz
U = 5 #V
T = array([]) + 273.15

### Execution
L1, L1_uncertainty, L12, L12_uncertainty = Exp1()
L2, L2_uncertainty = Exp2(L12, L12_uncertainty)
print(L1)
print(L12)
print(L2)
print(L1_uncertainty)
print(L12_uncertainty)
print(L2_uncertainty)
kappa, kappa_uncertainty = GetResultAndUncertainty(kappa_fun, [L1, L2, L12], True, [L1_uncertainty, L2_uncertainty, L12_uncertainty])
print(kappa)
print(kappa_uncertainty)
PlotInductivitiesAndKappa(loop_ratio, L1, L1_uncertainty, L2, L2_uncertainty, L12, L12_uncertainty, kappa, kappa_uncertainty)
R_coil1 = 25.3 * 50/500
R_coil2 = 25.3*N2/500
Exp3(R_coil1, R_coil2)

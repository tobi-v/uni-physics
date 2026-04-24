from matplotlib import pyplot as plt
from numpy import array, float64
from numpy.typing import NDArray
from pandas import read_csv
from tools.maths.angles import dms_to_rad
from tools.optics.prism import n_from_δmin
from tools.python.plot import ScatterWithErrorBars
from tools.statistics.linear_regression import Polyreg

angle_uncertainty = 0.1
angle_uncertainty = dms_to_rad(angle_uncertainty)

def Hg(α_0: float, hg_λ: NDArray[float64], hg_δmin_III: NDArray[float64], hg_δmin_II: NDArray[float64], hg_δmin_I: NDArray[float64]):
    fig, axs = plt.subplots(3, 1)
    for prism_no, ax, δ_min in zip(["III", "II", "I"], axs, [hg_δmin_III, hg_δmin_II, hg_δmin_I]):
        n, delN = n_from_δmin(α_0 - δ_min, uncertainty=True, delδ=angle_uncertainty)
        ScatterWithErrorBars(ax, hg_λ, n, y_absErr=delN, title=f"Prisma {prism_no}", xlabel="λ / nm", ylabel="n", label="Messwerte")
    plt.tight_layout()
    plt.close(fig)

    return Polyreg(α_0 - hg_δmin_III, 1/hg_λ, order=3)

def He(mapping, he_δmin: NDArray[float64]):
    print("=== δmin to λ for He ===")
    δmin_to_f, _, δmin_to_f_cov = mapping
    δmin = α_0 - he_δmin
    print(f"δmin: {δmin} +/- {angle_uncertainty:.3f}")

    he_λ = 1/δmin_to_f(δmin)
    print(f"λ: {he_λ} +/- {(1/(δmin_to_f_cov[0][0]**0.5) * he_δmin)} nm")

def Unknown(mapping, x_δmin: NDArray[float64]):
    print("=== δmin to λ for Unknown lamp ===")
    δmin_to_f, _, δmin_to_f_cov = mapping
    δmin = α_0 - x_δmin
    print(f"δmin: {δmin} +/- {angle_uncertainty:.3f}")

    he_λ = 1/δmin_to_f(δmin)
    print(f"λ: {he_λ} +/- {(1/(δmin_to_f_cov[0][0]**0.5) * x_δmin)} nm")

α_0 = 259.4
α_0 = dms_to_rad(α_0)
data = read_csv('20_data.csv')

hg_λ = data['Lambda'].to_numpy()
hg_δmin_III = data['III'].to_numpy()
hg_δmin_III = array([dms_to_rad(angle) for angle in hg_δmin_III])
hg_δmin_II = data['II'].to_numpy()
hg_δmin_II = array([dms_to_rad(angle) for angle in hg_δmin_II])
hg_δmin_I = data['I'].to_numpy()
hg_δmin_I = array([dms_to_rad(angle) for angle in hg_δmin_I])
mapping_fun = Hg(α_0, hg_λ, hg_δmin_III, hg_δmin_II, hg_δmin_I)

he_color = data['He III'].iloc[0:6].to_numpy()
he_δmin = data['Winkel_He'].iloc[0:6].to_numpy()
he_δmin = array([dms_to_rad(angle) for angle in he_δmin])
He(mapping_fun, he_δmin)

print("")
unb_color = data['Unbekannt III'].iloc[0:6].to_numpy()
x_δmin = data['Winkel_Unb'].iloc[0:6].to_numpy()
x_δmin = array([dms_to_rad(angle) for angle in x_δmin])
Unknown(mapping_fun, x_δmin)

plt.show()

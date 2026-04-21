from matplotlib import pyplot as plt
from numpy import array, float64
from numpy.typing import NDArray
from pandas import read_csv
from tools.maths.angles import dms_to_rad
from tools.optics.prism import n_from_δmin
from tools.python.plot import ScatterWithErrorBars

delta_angle = 0.1
delta_angle = dms_to_rad(delta_angle)

def Hg(α_0: float, hg_λ: NDArray[float64], hg_δmin_III: NDArray[float64], hg_δmin_II: NDArray[float64], hg_δmin_I: NDArray[float64]):
    fig, axs = plt.subplots(3, 1)
    for prism_no, ax, δ_min in zip(["III", "II", "I"], axs, [hg_δmin_III, hg_δmin_II, hg_δmin_I]):
        n, delN = n_from_δmin(α_0 - δ_min, uncertainty=True, delδ=delta_angle)
        ScatterWithErrorBars(ax, hg_λ, n, y_absErr=delN, title=f"Prisma {prism_no}", xlabel="λ / nm", ylabel="n", label="Messwerte")
    plt.tight_layout()
    plt.close(fig)

def He():
    pass

def Unbekannt():
    pass

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
Hg(α_0, hg_λ, hg_δmin_III, hg_δmin_II, hg_δmin_I)

he_color = data['He III'].iloc[0:6].to_numpy()
he_δmin = data['Winkel_He'].iloc[0:6].to_numpy()
he_δmin = array([dms_to_rad(angle) for angle in he_δmin])
He()

unb_color = data['Unbekannt III'].iloc[0:6].to_numpy()
unb_δmin = data['Winkel_Unb'].iloc[0:6].to_numpy()
unb_δmin = array([dms_to_rad(angle) for angle in unb_δmin])
Unbekannt()

plt.show()
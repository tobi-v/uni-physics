from matplotlib import pyplot as plt
from numpy import abs, argmax, array, diag, exp, linspace, loadtxt, nan, newaxis, pi, sqrt, std, sum
from os import path
from re import match
from scipy.fft import fft, fftfreq
from scipy.signal import find_peaks, hilbert
from scipy.optimize import curve_fit
from tools.signals.fourier import fft
from tools.maths.functions import Mean
from tools.statistics.uncertainty_calculation import GetResultAndUncertainty

data_dir = './dyn'

data_files = [
    'Messung_1_1-15_58g-0_09cm-10cm.txt',
    'Messung_1_1-15_58g-0_09cm-15cm.txt',
    'Messung_1_1-15_58g-0_09cm-20cm.txt',
    'Messung_1_2-15_58g-0_09cm-10cm.txt',
    'Messung_1_2-15_58g-0_09cm-15cm.txt',
    'Messung_1_2-15_58g-0_09cm-20cm.txt',
    'Messung_2_1-26_77g-0_05cm-10cm.txt',
    'Messung_2_1-26_77g-0_05cm-15cm.txt',
    'Messung_2_1-26_77g-0_05cm-20cm.txt',
    'Messung_2_2-26_77g-0_05cm-10cm.txt',
    'Messung_2_2-26_77g-0_05cm-15cm.txt',
    'Messung_2_2-26_77g-0_05cm-20cm.txt',
    'Messung_3_1-27_24g-0_05cm-10cm.txt',
    'Messung_3_1-27_24g-0_05cm-15cm.txt',
    'Messung_3_1-27_24g-0_05cm-20cm.txt',
    'Messung_3_2-27_24g-0_05cm-10cm.txt',
    'Messung_3_2-27_24g-0_05cm-15cm.txt',
    'Messung_3_2-27_24g-0_05cm-20cm.txt',
    'Messung_4_1-32_14g-0_29cm-10cm.txt',
    'Messung_4_1-32_14g-0_29cm-15cm.txt',
    'Messung_4_1-32_14g-0_29cm-20cm.txt',
    'Messung_4_2-32_14g-0_29cm-10cm.txt',
    'Messung_4_2-32_14g-0_29cm-15cm.txt',
    'Messung_4_2-32_14g-0_29cm-20cm.txt',
    'Messung_5_1-47_00g-0_12cm-10cm.txt',
    'Messung_5_1-47_00g-0_12cm-15cm.txt',
    'Messung_5_1-47_00g-0_12cm-20cm.txt',
    'Messung_5_2-47_00g-0_12cm-10cm.txt',
    'Messung_5_2-47_00g-0_12cm-15cm.txt',
    'Messung_5_2-47_00g-0_12cm-20cm.txt',
]

E_literature_ref = [('Stahl',210),('Aluminium',70),('Messing',96),
             ('Kupfer',120),('Titan',116)]  # [GPa]

a = 2.0e-2 # beam-width [m] is the same for all

Δm  = 0.5e-2  # [kg]
Δb  = 0.005e-2 # [m]
ΔL  = 0.1e-2   # [m]
Δa  = 0.02e-2  # [m]

# Nur diese Länge für den finalen E-Modul verwenden
# (kurze Länge → Einspannachgiebigkeit vernachlässigbar)
#L_ref = 10.0 # [cm]

# Numerical values from the instruction manual
beta_l_over_pi = array([0.59686, 1.49418, 2.50025, 3.49999])

def parse_filename(name):
    n = path.basename(name)
    m = match(r'Messung_(\d+)_(\d+)-(\d+)_(\d+)g-(\d+)_(\d+)cm-(\d+)cm.txt', n)
    if m:
        return (int(m.group(1)),                                # Balken
                int(m.group(2)),                                # Messung
                float(f"{m.group(3)}.{m.group(4)}") / 1000.,    # m [g]
                float(f"{m.group(5)}.{m.group(6)}") / 100.,     # b [m]
                float(m.group(7)) / 100.)                       # L [m]

    raise Exception(f"Mismatch in filename {name}.")

def load_data(data_path):
    d = loadtxt(data_path, skiprows=4)
    return d[:, 0], d[:, 1]

def find_trigger(v, window=50, threshold=0.015):
    for i in range(0, len(v) - window, 5):
        if v[i:i + window].std() > threshold:
            return max(0, i - 10)
    return 0

def expected_frequency(m, L, I):
    E_min = min(item[1] for item in E_literature_ref)*0.75
    E_max = max(item[1] for item in E_literature_ref)*1.25
    L_full = 0.3    # [m]
    β1 = beta_l_over_pi[0] * pi / L
    f_expected_lo = β1**2 / (2 * pi) * sqrt(E_min * 1e9 * I * L_full / m)
    f_expected_hi = β1**2 / (2 * pi) * sqrt(E_max * 1e9 * I * L_full / m)
    #print(f"E must lie between {E_min} and {E_max} for paramset m={m:.4f}, L={L:.2f}, I={I}, β_1={β1}")
    return max(1.0, f_expected_lo), min(500.0, f_expected_hi)

def f_from_E(m, I, E):
    β1 = beta_l_over_pi[0] * pi / L
    L_full = 0.3    # [m]
    return β1**2 / (2 * pi) * sqrt(E * 1e9 * I * L_full / m)

def exp_env(t, A0, delta0, A1, delta1):
    return A0 * exp(-delta0 * t) + A1 * exp(-delta1 * t)

def E_from_freq(m, I, f_1, β_1, ΔI, Δβ):
    def E_from_freqInner(m, I, f_1, β_1):
        L_full = 0.3    # [m]
        return (2*pi*f_1)**2 * m / (β_1**4 * I * L_full)
    
    #print(f"Calculating E with paramset m={m:.4f}, L={L:.2f}, I={I}, β_1={β_1}, f_1={f_1}")
    return GetResultAndUncertainty(E_from_freqInner,
                                    [m, I, f_1, β_1],
                                    True,
                                    [Δm, ΔI, 0, Δβ])

def I_x(a, b):
    def I_xInner(a, b):
        return a * b**3 / 12

    return GetResultAndUncertainty(I_xInner, [a, b], True, [Δa, Δb])

def β_1(L, ΔL):
    def β_1Inner(L):
        return beta_l_over_pi[0] * pi / L

    return GetResultAndUncertainty(β_1Inner, [L], True, [ΔL])

def get_peak_freq(t, dist, f_expected_lo, f_expected_hi):
    freqs, dist_ft = fft(t, dist)
    f_mask = (freqs >= f_expected_lo) & (freqs <= f_expected_hi)
    freqs = freqs[f_mask]
    dist_ft = dist_ft[f_mask]
    return freqs[argmax(dist_ft)]

# ============================================================
# ABSCHNITT 2: AUSWERTUNGSSCHLEIFE
# ============================================================

results = [[], [], [], [], []]

for filename in data_files:
    data_path = path.join(data_dir, filename)
    beam_nr, meas_nr, m, b, L = parse_filename(filename)

    print(f"{'─'*58}")
    print(f"Balken {beam_nr} Messung {meas_nr}  m={m:.4f} kg  b={b:.4f} m  L={L:.2f} m")

    I, ΔI = I_x(a, b)
    f_expected_lo, f_expected_hi = expected_frequency(m, L, I)
    print(f"Expected frequency range: {f_expected_lo} - {f_expected_hi} Hz.")


    t_all, dist_all = load_data(data_path)
    i0  = find_trigger(dist_all)
    t   = t_all[i0:] - t_all[i0]
    dist   = dist_all[i0:]

    peak_freq = get_peak_freq(t, dist, f_expected_lo, f_expected_hi)    
    print(f"Found peak frequency {peak_freq:.2f} Hz.")

    # Dämpfung
    env = abs(hilbert(dist - dist.mean()))
    noise = dist_all[:i0].std() if i0 > 20 else 0.005
    m_env = (t < min(3.0, t[-1])) & (env > 3*noise)
    delta0_fit = delta0_err = nan
    delta1_fit = delta1_err = nan
    pe_env = None

    p0e = [1., 10.0, 1., 1.]
    pe_env, ce = curve_fit(exp_env, t[m_env], env[m_env],
                            p0=p0e, maxfev=10000,
                            bounds=([0,0,0,0],[10,100,10,100]))
    pe_err = sqrt(diag(ce))
    delta0_fit = pe_env[1]; delta0_err = pe_err[1]
    A0 = pe_env[0]
    delta1_fit = pe_env[3]; delta1_err = pe_err[3]
    A1 = pe_env[2]
    print(f"A0 = {A0:.3f}, δ_0 = {delta0_fit:.3f} +/- {delta0_err:.3f} 1/s\nA1 = {A1:.3f}, δ_1 = {delta1_fit:.3f} +/- {delta1_err:.3f} 1/s")

    # E-Modul
    β, Δβ = β_1(L, ΔL)
    E, ΔE = E_from_freq(m, I, peak_freq, β, ΔI, Δβ)
    print(f"  E = ({E/1e9:.3f} ± {ΔE/1e9:.3f}) GPa")# associated with f={f_from_E(m, I, E)}")
    results[beam_nr-1].append((E, ΔE))

for ii, beam in enumerate(results):
    E_vals, ΔE_vals = zip(*beam)
    E_mean, ΔE_mean = Mean(E_vals, True, ΔE_vals)
    print(f"Balken {ii}: E = {E_mean/1e9:.3f} +/- {ΔE_mean/1e9:.3f}")

# ============================================================
# ABSCHNITT 3: PLOTS
# ============================================================

quit()
if results:
    massen = sorted(set(r['m'] for r in results))
    for masse in massen:
        subset = [r for r in results if r['m'] == masse]
        laengen = sorted(set(r['L'] for r in subset))
        for meas_nr in sorted(set(r['nr'] for r in subset)):
            ms_nr = sorted([r for r in subset if r['nr'] == meas_nr],
                           key=lambda x: x['L'])
            if not ms_nr:
                continue

            fig, axes = plt.subplots(len(laengen), 3,
                                     figsize=(15, 4*len(laengen)))
            if len(laengen) == 1:
                axes = axes[newaxis, :]

            r0 = ms_nr[0]
            # Titel: Referenz-E-Modul (nur L=10cm)
            r_ref = next((r for r in ms_nr if r['L'] == L_ref), None)
            E_ref_str = (f"E(L=10cm)=({r_ref['E']:.1f}±{r_ref['E_err']:.1f}) GPa"
                         if r_ref else "")
            fig.suptitle(
                f"Balken m={masse:.2f} g, b={r0['b']:.3f} cm — "
                f"Messung {meas_nr}    {E_ref_str}",
                fontsize=11, fontweight='bold'
            )

            for row, r in enumerate(ms_nr):
                is_ref = (r['L'] == L_ref)
                border_color = 'green' if is_ref else 'gray'

                # Panel 0: Zeitreihe
                ax = axes[row, 0]
                ax.plot(r['t_all'], r['v_all'], color='gray', lw=0.5)
                ax.axvline(r['t_all'][r['i0']], color='red', ls='--', lw=1.5)
                label = f"L={r['L']:.0f} cm"
                if is_ref:
                    label += "  ← Referenz (E-Modul)"
                ax.set_xlabel('$t$ [s]'); ax.set_ylabel('U [V]')
                ax.set_title(label, color='darkgreen' if is_ref else 'black',
                             fontweight='bold' if is_ref else 'normal')
                ax.grid(True, alpha=0.3)
                for spine in ax.spines.values():
                    spine.set_edgecolor(border_color)
                    spine.set_linewidth(2 if is_ref else 1)

                # Panel 1: FFT
                ax = axes[row, 1]
                mask_plt = (r['fp'] >= 0.5) & (r['fp'] <= min(350, 490))
                # ax.plot(r['fp'][mask_plt], r['ap'][mask_plt]*1000,
                #         color='darkorange', lw=0.8)
                ax.axvspan(r['f_lo'], r['f_hi'], alpha=0.12, color='green')
                ax.axvline(r['f1'], color='red', ls='--', lw=2.0,
                           label=f"$f_1$={r['f1']:.2f} Hz")
                ax.set_xlabel('$f$ [Hz]'); ax.set_ylabel('A [mV]')
                ax.set_title(f"FFT — $f_1$={r['f1']:.2f} Hz")
                ax.legend(fontsize=8); ax.grid(True, alpha=0.3)

                # Panel 2: Schwingung + Einhüllende
                ax = axes[row, 2]
                t_lim = min(3.0, r['t'][-1])
                ax.plot(r['t'], r['v'], color='steelblue', lw=0.6, alpha=0.85,
                        label='Signal')
                #ax.plot(r['t'], r['env'], color='black', lw=1.2, ls='--', alpha=0.6, label='Einhüllende')
#                if r['pe_env'] is not None:
#                    te = linspace(0, t_lim, 2000)
#                    ef = exp_env(te, *r['pe_env'])
#                    ax.plot(te,  ef, color='red', lw=2.0, label=f"δ={r['delta']:.2f} 1/s")
#                    ax.plot(te, -ef + 2*r['pe_env'][2], color='red', lw=2.0)
                ax.set_xlim(0, t_lim)
                ax.set_xlabel('$t$ ab Trigger [s]'); ax.set_ylabel('U [V]')
                E_str = f"E=({r['E']:.1f}±{r['E_err']:.1f}) GPa"
                if not is_ref:
                    E_str += ' [Einspannfehler!]'
                ax.set_title(E_str,
                             color='darkgreen' if is_ref else 'gray')
                ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

            plt.tight_layout()
            plotname = (f"plot_m{masse:.0f}g_messung{meas_nr}.pdf"
                        .replace('.', '_').replace('__', '_')
                        .replace('_pdf', '.pdf'))
            #plt.savefig(plotname)
            #plt.show()
            print(f"Plot: {plotname}")

# ============================================================
# ABSCHNITT 4: ZUSAMMENFASSUNG
# ============================================================
# Finaler E-Modul: NUR aus L=10cm (Einspanneffekt vernachlässigbar).
# Alle Längen zur Konsistenzprüfung angezeigt.



print(f"\n{'='*65}")
print(f"ZUSAMMENFASSUNG  (Finaler E-Modul aus L={L_ref:.0f} cm)")
print(f"Begründung: Bei L=10cm ist Einspannachgiebigkeit vernachlässigbar.")
print(f"{'='*65}")

massen = sorted(set(r['m'] for r in results))
for masse in massen:
    subset = [r for r in results if r['m'] == masse]
    r0 = subset[0]
    print(f"\nBalken  m={masse:.2f} g | b={r0['b']:.3f} cm")

    # Alle Längen anzeigen (Konsistenzcheck)
    print(f"  {'Nr':3} {'L[cm]':7} {'f_1[Hz]':10} {'E[GPa]':25}  {'Hinweis'}")
    print(f"  {'─'*65}")
    for r in sorted(subset, key=lambda x: (x['L'], x['nr'])):
        is_ref = (r['L'] == L_ref)
        hinweis = '← für E-Modul' if is_ref else '(Einspannfehler)'
        marker  = '**' if is_ref else '  '
        print(f"{marker} {r['nr']:3}  {r['L']:5.0f}    "
              f"{r['f1']:8.3f}    "
              f"({r['E']:.3f} ± {r['E_err']:.3f})    {hinweis}")

    # Nur L=10cm Messungen mitteln
    ref_ms = [r for r in subset if r['L'] == L_ref]
    if not ref_ms:
        print("  [INFO] Keine L=10cm Messung vorhanden.")
        continue

    E_ref = array([r['E'] for r in ref_ms])
    E_ref_err = array([r['E_err'] for r in ref_ms])
    w = 1.0 / E_ref_err**2
    E_mw = sum(w * E_ref) / sum(w)
    E_merr = 1.0 / sqrt(sum(w))

    print(f"  {'─'*65}")
    print(f"  Mittelwert (L=10cm): E = ({E_mw:.3f} ± {E_merr:.3f}) GPa")
    print(f"  Literaturvergleich:")
    best_mat = None; best_abw = 999
    for mat, El in E_literature_ref:
        abw = (E_mw - El) / El * 100
        marker = ''
        if abs(abw) < abs(best_abw):
            best_abw = abw; best_mat = mat
        print(f"    {mat:<12}: {El:.0f} GPa | Abw. = {abw:+.1f}%")
    if best_mat and abs(best_abw) < 25:
        print(f"  → Wahrscheinlichstes Material: {best_mat} (Abw. {best_abw:+.1f}%)")
    else:
        print(f"  → Kein Standardmetall passt gut!")
        print(f"    Bitte b mit Schieblehre nachmessen!")

    # Konsistenzcheck über alle Längen
    alle_E = [r['E_GPa'] for r in subset]
    E10_list = [r['E_GPa'] for r in subset if r['L_cm']==10]
    E20_list = [r['E_GPa'] for r in subset if r['L_cm']==20]
    ratio_str = f"{E10_list[0]/E20_list[0]:.2f}" if E10_list and E20_list else "n/a"
    print(f"  Konsistenzcheck (alle L): σ={std(alle_E):.1f} GPa, "
          f"E(10)/E(20)={ratio_str} "
          f"(idealer Wert: 1.00, typisch durch Einspannung: 1.5–2.0)")

print(f"\n{'='*65}")
print("Fertig.")
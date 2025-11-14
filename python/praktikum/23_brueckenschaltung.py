from numpy import array, linspace
from tools.python.checks import CheckLengths

def Ex01Poggendorf():
  print("=== Auswertung Poggendorf ===")
  def Ausmessen():
    # a)
    R_Feinsicherung = 2.3
    R_potentiometer_links = array([13.1, 22.9, 33.3, 46.5, 52.4, 62.2, 72.1, 81.9, 91.6, 101.3]) - R_Feinsicherung
    R_potentiometer_lvl = linspace(1,len(R_potentiometer_links), len(R_potentiometer_links))
    R_potentiometer_rechts = array([99.5, 198.3, 297.4, 396.7, 495, 594, 693, 793, 891, 990]) - R_Feinsicherung
    R_potentiometer_oben = array([97.8, 197.8, 298, 398, 497, 597, 697, 796, 896, 996])
    R_dekade_lvl = array([1, 10])
    R_dekade_links = array([10.2, 100.6])
    R_dekade_mitte = array([100.1, 1000])
    R_drehschalter_oben_rechts = array([12320, 4750, 1805, 679, 191.8, 178.9, ])
    # Dekade rechts kaputt
    # TODO Bestimmung der Potentiometerlevel mit linearer Regression
    
    # b) Batterie
    U_battery = 1.399

  def Poggendorf():
    U_A = 2 # Volt
    R_2 = array([400, 420, 440, 460, 480, 500, 520, 540, 560, 580])
    R_1 = array([258, 269, 283, 295, 308, 320, 333, 346, 358, 371])

  Ausmessen()

def Ex02Wheatstone01():
  print("=== Auswertung Wheatstone Teil 1 ===")
  def Res(R_1, R_2, R_3: float, name):
    R_x = R_2*R_3/R_1
    # TODO mean & var
    print("R_x_", name, ": " , R_x)
  R_1_blau = array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380]) # Dekade Ohm
  R_2_blau = array([166, 183, 200, 218, 234, 250, 267, 284, 301, 317]) # Potentiometer links Ohm
  R_3_blau = 191.9 # Ohm
  R_1_schwarz = R_1_blau + 300
  R_2_schwarz = array([613, 638, 662, 687, 712, 735, 760, 784, 809, 834])
  R_3_schwarz = 679 # Ohm
  R_1_C = array([300, 350, 400, 450, 500, 550, 600, 650, 700, 750])
  R_2_C = array([306, 364, 415, 468, 514, 562, 616, 670, 728, 764])
  C_3 = 682*10**-9 # Farad
  C_3_uncertainty = C_3 * 0.01
  R_1_RC = R_1_C
  R_2_RC = array([304, 360, 411, 464, 504, 561, 606, 660, 710, 767])
  RC_3_C = 336*10**-9 # Farad
  RC_3_R = 200 # Potentiometer rechts, Ohm
  RC_3_uncertainty = RC_3_C*0.01
  Res(R_1_blau, R_2_blau, R_3_blau, "blau")
  Res(R_1_schwarz, R_2_schwarz, R_3_schwarz, "schwarz")
  Res(R_1_C, R_2_C, C_3, "Kapazitaet")
  Res(R_1_RC, R_2_RC, RC_3_C, "RC_Kap")
  Res(R_1_RC, R_2_RC, RC_3_R, "RC_Res")

def Ex02Wheatstone02():
  print("=== Auswertung Wheatstone Teil 2 ===")
  del_R_2 = linspace(5, 50, 10)
  U_bridge = array([5, 5, 6, 6, 7, 8, 9, 9, 10, 11])*10**-3
  del_R_2_2 = -linspace(10, 50, 5)
  U_bridge2 = array([4, 6, 7, 9, 11])*10**-3


Ex01Poggendorf()

Ex02Wheatstone01()

Ex02Wheatstone02()
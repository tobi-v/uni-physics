from matplotlib.pyplot import show, subplots, tight_layout
from random import randint

N = 1000000

def roll_die():
    return randint(1, 6)


def roll_chain():
    five_six = False
    six_six = False
    ii = 0
    while True:
        ii += 1
        match roll_die():
            case 1:
                five_six = False
                six_six = False
            case 2:
                five_six = False
                six_six = False
            case 3:
                five_six = False
                six_six = False
            case 4:
                five_six = False
                six_six = False
            case 5:
                five_six = True
            case 6:
                if five_six:
                    return "5 6"#, ii
                if six_six:
                    return "6 6"#, ii
                six_six = True

fs = 0
ss = 0
for i in range(N):
    if roll_chain() == "5 6":
        fs += 1
    else:
        ss += 1

fig, ax = subplots()
ax.bar(["5 6", "6 6"], [fs, ss])
tight_layout()
show()
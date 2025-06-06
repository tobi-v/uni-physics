from numpy import polyfit, poly1d

def linreg(x, y):
    coeff, cov = polyfit(x, y, 1, cov=True)
    return poly1d(coeff), coeff, cov

def plotWithErrorBars(ax, x, y, linregFunc,
                      x_absErr=0, y_absErr=0, title="", xlabel="", ylabel=""):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x, linregFunc(x), '--k')
    ax.errorbar(x, y, fmt='k.', xerr=x_absErr, yerr=y_absErr, ecolor='r', capsize=1.5)

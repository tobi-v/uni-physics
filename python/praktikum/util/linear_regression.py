from numpy import polyfit, poly1d

### Also returns the coefficients of the curve and the covariance of the fit
def linreg(x, y):
    coeff, cov = polyfit(x, y, 1, cov=True)
    return poly1d(coeff), coeff[0], cov

def plotWithErrorBars(ax, x, y, linreg, cov, title=""):
    ax.set_title(title)
    ax.plot(x , y, 'go', x, linreg(x), '--k')
    ax.errorbar(x, y, fmt='ro', yerr=cov, ecolor='b')
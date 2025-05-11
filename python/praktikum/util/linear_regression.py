from numpy import polyfit, poly1d

### Also returns the coefficients of the curve and the covariance of the fit
def linreg(x, y):
    coeff, cov = polyfit(x, y, 1, cov=True)
    return poly1d(coeff), coeff[0], cov
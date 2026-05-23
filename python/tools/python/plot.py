def DefaultPlot(ax, x, y, title="", label="", xlabel="", ylabel="", c="--k"):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x, y, c, label=label)
    ax.grid(visible=True)
    ax.legend()

def DefaultScatter(ax, x, y, title="", label="", xlabel="", ylabel="", c='k'):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.scatter(x, y, c=c, label=label)
    ax.grid(visible=True)
    ax.legend()
    
def ScatterWithErrorBars(ax, x, y,
                      x_absErr=0, y_absErr=0, title="", label="", xlabel="", ylabel="", data_color="k.", error_color="r", legend_loc='best', grid=True):
    ax.set_title(title, fontsize = 20)
    ax.set_xlabel(xlabel, fontsize = 18)
    ax.set_ylabel(ylabel, fontsize = 18)
    ax.tick_params(labelsize=14)
    ax.errorbar(x, y, fmt=data_color, xerr=x_absErr, yerr=y_absErr, label=label, ecolor=error_color, capsize=1.5)
    ax.legend(loc=legend_loc, fontsize=14)
    ax.grid(visible=grid)
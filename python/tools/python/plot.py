def DefaultPlot(ax, x, y, title="", label="", xlabel="", ylabel=""):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(x, y, '--k', label=label)
    ax.grid()

def DefaultScatter(ax, x, y, title="", label="", xlabel="", ylabel=""):
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.scatter(x, y, c='k', label=label)
    ax.grid()
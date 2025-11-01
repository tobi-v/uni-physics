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
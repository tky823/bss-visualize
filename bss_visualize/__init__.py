import matplotlib.pyplot as plt

from .boxplot import boxplot_by_group
from .plot import plot_by_elapsed_time, plot_by_iteration

__version__ = "0.0.0"

__all__ = ["set_tex_style", "boxplot_by_group", "plot_by_elapsed_time", "plot_by_iteration"]


def set_tex_style():
    params = {
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": ["Computer Modern Serif"],
    }

    plt.rcParams.update(params)

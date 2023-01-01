from typing import Dict, List, Optional, Tuple

import numpy as np
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

axis_linewidth = 2
majorgrid_linewidth = 1.5


def plot_iteration(
    ax: Axes,
    data: Dict,
    labels: List[str] = None,
    n_iter: Optional[int] = None,
    marker: str = "o",
    markersize: int = 10,
    show_zero_xaxis: bool = True,
    palette: Optional[List[Tuple[float, float, float]]] = None,
) -> List[Line2D]:
    iterations = {}

    if palette is None:
        palette = sns.color_palette()

    for label_idx in range(len(labels)):
        label = labels[label_idx]

        if n_iter is None:
            iterations[label] = np.arange(len(data[label]))
        else:
            iterations[label] = np.arange(n_iter + 1)

    if show_zero_xaxis:
        ax.axhline(y=0, color="black", linewidth=axis_linewidth)

    handles = _plot(
        ax,
        data,
        iterations,
        labels=labels,
        n_iter=n_iter,
        marker=marker,
        markersize=markersize,
        palette=palette,
    )

    return handles


def _plot(
    ax: Axes,
    y: Dict,
    x: Dict,
    labels: List[str] = None,
    n_iter: Optional[int] = None,
    marker: str = "o",
    markersize: int = 10,
    palette: Optional[List[Tuple[float, float, float]]] = None,
):
    if palette is None:
        palette = sns.color_palette()

    handles = []

    for label_idx in range(len(labels)):
        label = labels[label_idx]

        if n_iter is None:
            _x = x[label]
            _y = y[label]
        else:
            _x = x[label][: n_iter + 1]
            _y = y[label][: n_iter + 1]

        (handle,) = ax.plot(
            _x,
            _y,
            color=palette[label_idx],
            marker=marker,
            markersize=markersize,
        )

        handles.append(handle)

    ax.set_axisbelow(True)
    ax.grid(
        b=True,
        which="major",
        color="lightgray",
        linestyle="--",
        linewidth=majorgrid_linewidth,
        axis="y",
    )

    return handles

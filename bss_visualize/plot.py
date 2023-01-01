from typing import Dict, List, Optional, Tuple

import numpy as np
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

axis_linewidth = 2
majorgrid_linewidth = 1.5


def plot_by_iteration(
    ax: Axes,
    data: Dict,
    labels: List[str] = None,
    n_iter: Optional[int] = None,
    step: int = 1,
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
        step=step,
        labels=labels,
        marker=marker,
        markersize=markersize,
        palette=palette,
    )

    return handles


def plot_by_elapsed_time(
    ax: Axes,
    data: Dict,
    elapsed_time: Dict,
    labels: List[str] = None,
    n_iter: Optional[int] = None,
    step: int = 1,
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
            iterations[label] = elapsed_time[label]
        else:
            iterations[label] = elapsed_time[label][: n_iter + 1]

    if show_zero_xaxis:
        ax.axhline(y=0, color="black", linewidth=axis_linewidth)

    handles = _plot(
        ax,
        data,
        iterations,
        step=step,
        labels=labels,
        marker=marker,
        markersize=markersize,
        palette=palette,
    )

    return handles


def _plot(
    ax: Axes,
    y: Dict,
    x: Dict,
    step: int = 1,
    labels: List[str] = None,
    marker: str = "o",
    markersize: int = 10,
    palette: Optional[List[Tuple[float, float, float]]] = None,
):
    if palette is None:
        palette = sns.color_palette()

    handles = []

    for label_idx in range(len(labels)):
        label = labels[label_idx]
        _x = x[label]
        _y = y[label][: len(_x)]

        (handle,) = ax.plot(
            _x[::step],
            _y[::step],
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

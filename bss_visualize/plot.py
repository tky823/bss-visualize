from typing import Dict, List, Optional, Tuple, Union

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
    linestyle: Union[str, List[str]] = "-",
    marker: Union[str, List[str]] = "o",
    markersize: Union[int, List[int]] = 10,
    markerfacecolor: Union[str, List[str]] = None,
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
        linestyle=linestyle,
        marker=marker,
        markersize=markersize,
        markerfacecolor=markerfacecolor,
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
    linestyle: Union[str, List[str]] = "-",
    marker: Union[str, List[str]] = "o",
    markersize: Union[int, List[int]] = 10,
    markerfacecolor: Union[str, List[str]] = None,
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
        linestyle=linestyle,
        marker=marker,
        markersize=markersize,
        markerfacecolor=markerfacecolor,
        palette=palette,
    )

    return handles


def _plot(
    ax: Axes,
    y: Dict,
    x: Dict,
    step: int = 1,
    labels: List[str] = None,
    linestyle: Union[str, List[str]] = "-",
    marker: Union[str, List[str]] = "o",
    markersize: Union[int, List[int]] = 10,
    markerfacecolor: Union[str, List[str]] = None,
    palette: Optional[List[Tuple[float, float, float]]] = None,
):
    if palette is None:
        palette = sns.color_palette()

    if type(linestyle) is not list:
        linestyle = [linestyle] * len(labels)

    if type(marker) is not list:
        marker = [marker] * len(labels)

    if type(markersize) is not list:
        markersize = [markersize] * len(labels)

    handles = []

    for label_idx in range(len(labels)):
        label = labels[label_idx]
        _x = x[label]
        _y = y[label][: len(_x)]

        kwargs = {}

        if markerfacecolor is not None:
            if type(markerfacecolor) is list:
                kwargs["markerfacecolor"] = markerfacecolor[label_idx]
            else:
                kwargs["markerfacecolor"] = markerfacecolor

        (handle,) = ax.plot(
            _x[::step],
            _y[::step],
            color=palette[label_idx],
            linestyle=linestyle[label_idx],
            marker=marker[label_idx],
            markersize=markersize[label_idx],
            **kwargs,
        )

        handles.append(handle)

    ax.set_axisbelow(True)
    ax.grid(
        visible=True,
        which="major",
        color="lightgray",
        linestyle="--",
        linewidth=majorgrid_linewidth,
        axis="y",
    )

    return handles

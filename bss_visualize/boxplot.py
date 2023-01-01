from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

box_alpha = 0.3
box_edgewidth = 2
axis_linewidth = 2
majorgrid_linewidth = 1.5


def boxplot_by_group(
    ax: Axes,
    data: Dict,
    labels: List[str],
    names: List[str],
    width: Optional[Union[float, List[float]]] = None,
    margin: Optional[float] = None,
    show_zero_xaxis: bool = True,
    palette: Optional[List[Tuple[float, float, float]]] = None,
) -> List[Line2D]:
    if palette is None:
        palette = sns.color_palette()

    if width is None:
        width = 0.5 / len(names)
        widths = [width] * len(labels)
    elif type(width) is float:
        widths = width
    elif type(width) is float:
        widths = [width] * len(labels)
    else:
        raise ValueError("Invalid type of width is detected.")

    if margin is None:
        margin = 0.75 / len(names)

    if show_zero_xaxis:
        ax.axhline(y=0, color="black", linewidth=axis_linewidth)

    handles: List[Line2D] = []

    for name_idx in range(len(names)):
        name = names[name_idx]
        _data = [data[label][name] for label in labels]
        positions = np.arange(len(labels)) + margin * name_idx - 0.5 * margin * (len(names) - 1)
        boxplot = ax.boxplot(
            _data,
            positions=positions,
            widths=widths,
            labels=labels,
            patch_artist=True,
        )

        for xticklabel_idx in range(len(labels)):
            color = palette[name_idx]
            r, g, b = color

            boxplot["boxes"][xticklabel_idx].set_facecolor((r, g, b, box_alpha))
            boxplot["boxes"][xticklabel_idx].set(edgecolor=color, linewidth=box_edgewidth)
            boxplot["medians"][xticklabel_idx].set(color=color, linewidth=box_edgewidth)
            boxplot["fliers"][xticklabel_idx].set(
                markeredgecolor=color, markeredgewidth=box_edgewidth
            )
            boxplot["whiskers"][2 * xticklabel_idx].set(color=color, linewidth=box_edgewidth)
            boxplot["whiskers"][2 * xticklabel_idx + 1].set(color=color, linewidth=box_edgewidth)
            boxplot["caps"][2 * xticklabel_idx].set(color=color, linewidth=box_edgewidth)
            boxplot["caps"][2 * xticklabel_idx + 1].set(color=color, linewidth=box_edgewidth)

            if xticklabel_idx == 0:
                handles.append(boxplot["boxes"][xticklabel_idx])

    ax.set_axisbelow(True)
    ax.grid(
        b=True,
        which="major",
        color="lightgray",
        linestyle="--",
        linewidth=majorgrid_linewidth,
        axis="y",
    )

    xticks = np.arange(len(labels))
    ax.set_xticks(xticks)
    ax.set_xticklabels(labels)

    return handles

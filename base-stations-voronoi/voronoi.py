import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

def build_voronoi(stations, xlim=(0, 100), ylim=(0, 100), show_labels=True):
    """
    Строит диаграмму Вороного по координатам базовых станций.

    :param stations: список кортежей [(x1, y1), (x2, y2), ...] или np.ndarray (N, 2)
    :param xlim: границы области по оси X
    :param ylim: границы области по оси Y
    :param show_labels: показывать ли подписи базовых станций
    """
    points = np.asarray(stations, dtype=float)
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("Coordinates data error, required (N, 2)")
    if len(points) < 3:
        raise ValueError("Minimum 3 BS acquired")

    padding = max(xlim[1] - xlim[0], ylim[1] - ylim[0]) * 10
    far_points = np.array([
        [xlim[0] - padding, ylim[0] - padding],
        [xlim[0] - padding, ylim[1] + padding],
        [xlim[1] + padding, ylim[0] - padding],
        [xlim[1] + padding, ylim[1] + padding],
    ])
    all_points = np.vstack([points, far_points])

    vor = Voronoi(all_points)

    fig, ax = plt.subplots(figsize=(9, 9))
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')
    ax.set_title("Voronoi for Base Stations")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")

    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        # пропускаем рёбра, образованные фиктивными точками
        if p1 >= len(points) or p2 >= len(points):
            continue
        if v1 == -1 or v2 == -1:
            continue
        seg = vor.vertices[[v1, v2]]
        ax.plot(seg[:, 0], seg[:, 1], 'k-', linewidth=1.2)

    ax.scatter(points[:, 0], points[:, 1],
               c='red', s=80, zorder=5, edgecolors='darkred',
               label='Base Stations')

    if show_labels:
        for i, (x, y) in enumerate(points):
            ax.annotate(f"BS{i + 1}\n({x:.0f}, {y:.0f})",
                        xy=(x, y), xytext=(6, 6),
                        textcoords='offset points',
                        fontsize=9, color='darkred')

    ax.legend(loc='upper right')
    ax.grid(alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.show()

    return vor
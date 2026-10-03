import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib.patches import Polygon


def input_stations():
    """Запрашивает координаты базовых станций у пользователя"""
    print("Input Base Station coordinates in format: x y")
    stations = []
    while True:
        raw = input(f"BS{len(stations) + 1}: ").strip()
        if not raw:
            break
        try:
            x, y = map(float, raw.replace(',', '.').split())
            stations.append((x, y))
        except ValueError:
            print("Input Error")
    return stations
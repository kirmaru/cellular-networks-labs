from voronoi import *
from bs_input import *


if __name__ == "__main__":
    # stations = input_stations()

    stations = [
        (10, 20),
        (35, 70),
        (60, 30),
        (80, 60),
        (25, 45),
        (55, 85),
        (90, 15),
    ]

    build_voronoi(stations, xlim=(0, 100), ylim=(0, 100))
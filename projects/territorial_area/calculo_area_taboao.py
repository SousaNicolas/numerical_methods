"""Approximate area of a manually traced region near Taboao, Brazil.

Educational demonstration of linear interpolation and the composite
trapezoidal rule applied to a closed polygonal boundary.
Coordinates are locally projected approximations expressed in kilometers.
They do NOT define official administrative neighborhood boundaries.
"""

POINTS_KM = [
    (1.9427, 2.7213),   # A
    (4.1308, 1.2704),   # B
    (7.6494, 2.7738),   # C
    (8.2445, 3.6129),   # D
    (7.4393, 5.6935),   # E
    (6.0214, 7.0049),   # F
    (5.7413, 8.2465),   # G
    (5.4262, 9.1559),   # H
    (5.3737, 10.8349),  # I
    (4.5510, 10.8524),  # J
    (1.7151, 8.1940),   # K
    (0.9799, 3.8577),   # M
]


def linear_interpolation(p1, p2, t):
    """Interpolate between endpoints, with 0 <= t <= 1."""
    x1, y1 = p1
    x2, y2 = p2
    return x1 + t * (x2 - x1), y1 + t * (y2 - y1)


def area_by_trapezoids(points):
    """Integrate x dy around the closed piecewise-linear boundary."""
    total = 0.0
    n = len(points)
    if n < 3:
        raise ValueError("At least three vertices are required.")

    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        x1, y1 = linear_interpolation(p1, p2, 0.0)
        x2, y2 = linear_interpolation(p1, p2, 1.0)
        total += (x1 + x2) / 2.0 * (y2 - y1)

    return abs(total)


def main():
    area_km2 = area_by_trapezoids(POINTS_KM)
    geogebra_area_km2 = 41.96  # Rounded GeoGebra display
    my_maps_area_km2 = 42.0    # Rounded Google My Maps display

    absolute_difference = abs(area_km2 - my_maps_area_km2)
    percent_difference = absolute_difference / my_maps_area_km2 * 100.0

    print("NUMERICAL METHODS - TERRITORIAL AREA")
    print("------------------------------------")
    print(f"Vertices: {len(POINTS_KM)}")
    print("Boundary: linear interpolation")
    print("Integration: composite trapezoidal rule on closed contour")
    print(f"Python area:      {area_km2:.4f} km²")
    print(f"GeoGebra area:    {geogebra_area_km2:.2f} km²")
    print(f"Google My Maps:   {my_maps_area_km2:.1f} km²")
    print(f"Absolute difference: {absolute_difference:.4f} km²")
    print(f"Percentage difference: {percent_difference:.4f}%")
    print("Note: My Maps and GeoGebra display rounded values.")


if __name__ == "__main__":
    main()

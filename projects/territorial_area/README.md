# Territorial area approximation

An introductory numerical methods exercise using **linear interpolation** and the **composite trapezoidal rule**.

## Problem

Estimate the area enclosed by 12 vertices traced manually in Google My Maps in the Taboão region of São Bernardo do Campo, São Paulo, Brazil. The vertices were converted approximately to local Cartesian coordinates in kilometers and visualized in GeoGebra.

**Important:** The polygon is an educational, manually drawn approximation. It does not represent an official administrative boundary.

## Method

Each consecutive pair of vertices is joined by linear interpolation:

```text
x(t) = x_i + t (x_(i+1) - x_i)
y(t) = y_i + t (y_(i+1) - y_i), 0 <= t <= 1
```

The area is obtained by applying the trapezoidal rule to the closed contour integral of `x dy`:

```text
A = | sum_i [(x_i + x_(i+1))/2] * [y_(i+1) - y_i] |
```

Because the edges are straight, the rule is exact for the specified polygon (apart from coordinate rounding). It does not establish the accuracy of the traced geographic boundary.

## Results

| Source | Area |
| --- | ---: |
| Python | 41.9603 km² |
| GeoGebra (rounded display) | 41.96 km² |
| Google My Maps (rounded display) | 42.0 km² |

The difference between the Python result and the rounded Google My Maps display is approximately **0.0397 km² (0.0945%)**. This is not a comparison against an independent official boundary and is consistent with display rounding.

## Run

Requires Python 3; no third-party packages.

```bash
python projects/territorial_area/calculo_area_taboao.py
```

Developed for an undergraduate Numerical Methods practical activity.

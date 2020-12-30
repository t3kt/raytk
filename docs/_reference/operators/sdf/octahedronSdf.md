---
layout: operator
title: octahedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/octahedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.octahedronSdf/
op:
  name: octahedronSdf
  summary: |
    An octahedron, with its corners facing the axes.
  opType: raytk.operators.sdf.octahedronSdf
  category: sdf
  parameters:
    - name: Translate
      label: Translate
      summary: |
        Shifts the center of the shape.
    - name: Radius
      label: Radius
      summary: |
        The size of the shape.
    - name: Shapetype
      label: Shape Type
      summary: |
        Advanced parameter that chooses between different types of calculations.
      menuOptions:
        - name: exact
          label: Exact
          description: |
            Provides more accuracy but can produce roughness around the edges.
        - name: bound
          label: Bound (Not Exact)
          description: |
            Less accurate but less rough around the edges.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# octahedronSdf

Category: sdf



An octahedron, with its corners facing the axes.
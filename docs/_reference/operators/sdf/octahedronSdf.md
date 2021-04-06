---
layout: operator
title: octahedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/octahedronSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.octahedronSdf/
op:
  category: sdf
  name: octahedronSdf
  opType: raytk.operators.sdf.octahedronSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Shifts the center of the shape.
  - label: Radius
    name: Radius
    summary: The size of the shape.
  - label: Function
    menuOptions:
    - description: Provides more accuracy but can produce roughness around the edges.
      label: Exact
      name: exact
    - description: Less accurate but less rough around the edges.
      label: Bound (Not Exact)
      name: bound
    name: Function
    summary: Advanced parameter that chooses between different types of calculations.
  summary: An octahedron, with its corners facing the axes.

---


An octahedron, with its corners facing the axes.
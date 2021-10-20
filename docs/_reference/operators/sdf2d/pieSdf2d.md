---
layout: operator
title: pieSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/pieSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.pieSdf2d/
op:
  category: sdf2d
  name: pieSdf2d
  opType: raytk.operators.sdf2d.pieSdf2d
  parameters:
  - label: Radius
    name: Radius
    summary: The distance from the center to the outer edge.
  - label: Angle
    name: Angle
    summary: The width of the slice in degrees.
  - label: Rotate
    name: Rotate
    summary: Rotation for the slice in degrees.
  - label: Shape
    menuOptions:
    - label: Slice
      name: slice
    - label: Ring
      name: ring
    name: Shape
  - label: Inner Radius
    name: Innerradius
  summary: SDF for a 2D pie-slice shape.

---


SDF for a 2D pie-slice shape.
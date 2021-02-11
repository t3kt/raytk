---
layout: operator
title: prismSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/prismSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.prismSdf/
op:
  category: sdf
  name: prismSdf
  opType: raytk.operators.sdf.prismSdf
  parameters:
  - label: Prism Type
    menuOptions:
    - label: Triangle
      name: tri
    - label: Square
      name: square
    - label: Hexagon
      name: hex
    - label: Octogon
      name: octogon
    name: Prismtype
    summary: The number of sides of the prism.
  - label: Translate
    name: Translate
    summary: Moves the center of the prism.
  - label: Radius
    name: Radius
    summary: The radius of the prism.
  - label: Height
    name: Height
    summary: The height / length of the prism.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: A prism shape, like a cylinder but with flat sides, along the z axis.

---

# prismSdf

Category: sdf



A prism shape, like a cylinder but with flat sides, along the z axis.
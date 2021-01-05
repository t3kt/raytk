---
layout: operator
title: prismSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/prismSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.prismSdf/
op:
  name: prismSdf
  summary: A prism shape, like a cylinder but with flat sides, along the z axis.
  opType: raytk.operators.sdf.prismSdf
  category: sdf
  parameters:
    - name: Prismtype
      label: Prism Type
      summary: |
        The number of sides of the prism.
      menuOptions:
        - name: tri
          label: Triangle
        - name: square
          label: Square
        - name: hex
          label: Hexagon
        - name: octogon
          label: Octogon
    - name: Translate
      label: Translate
      summary: |
        Moves the center of the prism.
    - name: Radius
      label: Radius
      summary: |
        The radius of the prism.
    - name: Height
      label: Height
      summary: |
        The height / length of the prism.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# prismSdf

Category: sdf



A prism shape, like a cylinder but with flat sides, along the z axis.
---
layout: operator
title: solidAngleSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/solidAngleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.solidAngleSdf/
op:
  name: solidAngleSdf
  summary: |
    A conical slice of a sphere.
  detail: |
    Similar to `coneSdf` but with the base rounded.
  opType: raytk.operators.sdf.solidAngleSdf
  category: sdf
  parameters:
    - name: Translate
      label: Translate
      summary: |
        Moves the tip of the shape.
    - name: Angle
      label: Angle
      summary: |
        The angle width of the slice.
    - name: Radius
      label: Radius
      summary: |
        The radius of the sphere that the shape is based one, equivalent to the distance from the tip to the base.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# solidAngleSdf

Category: sdf



A conical slice of a sphere.

Similar to `coneSdf` but with the base rounded.
---
layout: operator
title: planeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/planeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.planeSdf/
op:
  category: sdf
  name: planeSdf
  opType: raytk.operators.sdf.planeSdf
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    summary: Which axis the plane faces.
  - label: Offset
    name: Offset
    summary: Shifts the plane forwards or backwards along the axis that it faces.
  summary: An infinite plane on the x, y, or z axis.

---


An infinite plane on the x, y, or z axis.
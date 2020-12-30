---
layout: operator
title: planeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/planeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.planeSdf/
op:
  name: planeSdf
  summary: |
    An infinite plane on the x, y, or z axis.
  opType: raytk.operators.sdf.planeSdf
  category: sdf
  parameters:
    - name: Axis
      label: Axis
      summary: |
        Which axis the plane faces.
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Offset
      label: Offset
      summary: |
        Shifts the plane forwards or backwards along the axis that it faces.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# planeSdf

Category: sdf



An infinite plane on the x, y, or z axis.
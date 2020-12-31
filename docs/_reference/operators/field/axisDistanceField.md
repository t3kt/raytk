---
layout: operator
title: axisDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/axisDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.axisDistanceField/
op:
  name: axisDistanceField
  summary: A float field that provides the distance from a specific point along a single axis.
  opType: raytk.operators.field.axisDistanceField
  category: field
  parameters:
    - name: Axis
      label: Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Center
      label: Center
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: float
          label: 1D
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# axisDistanceField

Category: field



A float field that provides the distance from a specific point along a single axis.
---
layout: operator
title: constantField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/constantField
redirect_from:
  - /reference/opType/raytk.operators.field.constantField/
op:
  name: constantField
  summary: A float or vector field that evaluates to a constant value.
  opType: raytk.operators.field.constantField
  category: field
  parameters:
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: float
          label: 1D
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Returntype
      label: Return Type
      menuOptions:
        - name: float
          label: Float
        - name: vec4
          label: Vector
    - name: Contexttype
      label: Context Type
      menuOptions:
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
    - name: Value
      label: Value
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# constantField

Category: field



A float or vector field that evaluates to a constant value.
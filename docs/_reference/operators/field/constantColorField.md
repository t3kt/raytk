---
layout: operator
title: constantColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/constantColorField
redirect_from:
  - /reference/opType/raytk.operators.field.constantColorField/
op:
  name: constantColorField
  summary: A vector field that evaluates to a constant color value.
  detail: |
    This is the same as `constantField`, but the parameter is specified as a color instead of arbitrary float values.
  opType: raytk.operators.field.constantColorField
  category: field
  parameters:
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
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
    - name: Color
      label: Color
    - name: Alpha
      label: Alpha
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# constantColorField

Category: field



A vector field that evaluates to a constant color value.

This is the same as `constantField`, but the parameter is specified as a color instead of arbitrary float values.
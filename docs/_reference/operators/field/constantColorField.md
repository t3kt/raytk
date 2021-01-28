---
layout: operator
title: constantColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/constantColorField
redirect_from:
  - /reference/opType/raytk.operators.field.constantColorField/
op:
  category: field
  detail: This is the same as `constantField`, but the parameter is specified as a
    color instead of arbitrary float values.
  name: constantColorField
  opType: raytk.operators.field.constantColorField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
  - label: Color
    name: Color
  - label: Alpha
    name: Alpha
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: A vector field that evaluates to a constant color value.

---

# constantColorField

Category: field



A vector field that evaluates to a constant color value.

This is the same as `constantField`, but the parameter is specified as a color instead of arbitrary float values.
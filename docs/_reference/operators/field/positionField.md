---
layout: operator
title: positionField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/positionField
redirect_from:
  - /reference/opType/raytk.operators.field.positionField/
op:
  category: field
  name: positionField
  opType: raytk.operators.field.positionField
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
    - label: Ray Context
      name: RayContext
    name: Contexttype
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: A vector field that evaluates to the coordinates in space.

---

# positionField

Category: field



A vector field that evaluates to the coordinates in space.
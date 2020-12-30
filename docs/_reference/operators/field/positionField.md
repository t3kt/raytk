---
layout: operator
title: positionField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/positionField
redirect_from:
  - /reference/opType/raytk.operators.field.positionField/
op:
  name: positionField
  summary: |
    A vector field that evaluates to the coordinates in space.
  opType: raytk.operators.field.positionField
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
        - name: RayContext
          label: Ray Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# positionField

Category: field



A vector field that evaluates to the coordinates in space.
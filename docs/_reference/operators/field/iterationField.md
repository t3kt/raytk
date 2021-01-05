---
layout: operator
title: iterationField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/iterationField
redirect_from:
  - /reference/opType/raytk.operators.field.iterationField/
op:
  name: iterationField
  summary: Field that returns the current iteration, from a downstream OP.
  opType: raytk.operators.field.iterationField
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
    - name: Iterationmode
      label: Iteration Mode
      menuOptions:
        - name: index
          label: Index
        - name: scaledindex
          label: Scaled Index
        - name: full
          label: Full Data
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# iterationField

Category: field



Field that returns the current iteration, from a downstream OP.
---
layout: operator
title: pointDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/pointDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.pointDistanceField/
op:
  name: pointDistanceField
  summary: A float field that provides the distance from a specific point in space.
  opType: raytk.operators.field.pointDistanceField
  category: field
  parameters:
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

# pointDistanceField

Category: field



A float field that provides the distance from a specific point in space.
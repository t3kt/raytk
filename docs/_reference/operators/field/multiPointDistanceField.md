---
layout: operator
title: multiPointDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/multiPointDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.multiPointDistanceField/
op:
  name: multiPointDistanceField
  summary: |
    A vector field that provides the distance from 4 specific points in space (one for each part of the vector).
  opType: raytk.operators.field.multiPointDistanceField
  category: field
  parameters:
    - name: Point1
      label: Point 1
    - name: Point2
      label: Point 2
    - name: Point3
      label: Point 3
    - name: Point4
      label: Point 4
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
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# multiPointDistanceField

Category: field



A vector field that provides the distance from 4 specific points in space (one for each part of the vector).
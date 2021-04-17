---
layout: operator
title: multiPointDistanceField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/multiPointDistanceField
redirect_from:
  - /reference/opType/raytk.operators.field.multiPointDistanceField/
op:
  category: field
  name: multiPointDistanceField
  opType: raytk.operators.field.multiPointDistanceField
  parameters:
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
  - label: Point 3
    name: Point3
  - label: Point 4
    name: Point4
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  summary: A vector field that provides the distance from 4 specific points in space
    (one for each part of the vector).

---


A vector field that provides the distance from 4 specific points in space (one for each part of the vector).
---
layout: operator
title: valuePointsField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/valuePointsField
redirect_from:
  - /reference/opType/raytk.operators.field.valuePointsField/
op:
  category: field
  name: valuePointsField
  opType: raytk.operators.field.valuePointsField
  parameters:
  - label: Weight Mode
    menuOptions:
    - label: Nearest
      name: nearest
    - label: Linear Weight
      name: linearweight
    - label: Linear Nearest
      name: linearnearest
    name: Weightmode
  - label: Point 1
    name: Point1
  - label: Value 1
    name: Value1
  - label: Point 2
    name: Point2
  - label: Value 2
    name: Value2
  - label: Point 3
    name: Point3
  - label: Value 3
    name: Value3
  - label: Point 4
    name: Point4
  - label: Value 4
    name: Value4
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
  status: alpha

---

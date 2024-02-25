---
layout: operator
title: polarCoordField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/polarCoordField
redirect_from:
  - /reference/opType/raytk.operators.field.polarCoordField/
op:
  category: field
  name: polarCoordField
  opType: raytk.operators.field.polarCoordField
  parameters:
  - label: Format
    menuOptions:
    - label: Polar (Dist,Angle,AxisPos)
      name: polar
    - label: Spherical (Dist,Angle1,Angle2)
      name: spherical
    - label: Angle
      name: angle
    - label: Plane Distance
      name: planedist
    - label: Spherical Distance
      name: dist
    name: Format
    readOnlyHandling: baked
    regularHandling: baked
  - label: Angle Unit
    menuOptions:
    - label: Ratio (0..1)
      name: ratio
    - label: Degrees
      name: degrees
    - label: Radians
      name: radians
    name: Angleunit
    readOnlyHandling: baked
    regularHandling: baked
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The center point of the polar coordinates.
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - name: Contexttype
  status: beta
  summary: A field that produces various types of polar coordinates.
  thumb: assets/images/reference/operators/field/polarCoordField_thumb.png

---


A field that produces various types of polar coordinates.
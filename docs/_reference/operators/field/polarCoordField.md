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
  - label: Angle Unit
    menuOptions:
    - label: Ratio (0..1)
      name: ratio
    - label: Degrees
      name: degrees
    - label: Radians
      name: radians
    name: Angleunit
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Center
    name: Center
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
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
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
    - label: ParticleContext
      name: ParticleContext
    name: Contexttype
  status: beta

---

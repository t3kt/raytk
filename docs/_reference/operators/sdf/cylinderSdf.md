---
layout: operator
title: cylinderSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/cylinderSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.cylinderSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec3
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
    summary: Optional field used to control the radius of the cylinder. If it uses
      1D coordinates, it is given the position along the axis. For 3D coordinates,
      it is given the raw position.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec3
    label: Height Field
    name: height_field_definition_in
    returnTypes:
    - float
  name: cylinderSdf
  opType: raytk.operators.sdf.cylinderSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Shifts the center of the cylinder.
  - label: Radius
    name: Radius
    summary: The radius of the cylinder.
  - label: Height
    name: Height
    summary: The height of the cylinder, along the selected axis.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: SDF for a cylinder.

---


SDF for a cylinder.
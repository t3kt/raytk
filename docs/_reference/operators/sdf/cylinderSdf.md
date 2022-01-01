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
    - ParticleContext
    coordTypes:
    - vec3
    label: Radius Field
    name: radiusField
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
    - ParticleContext
    coordTypes:
    - vec3
    label: Height Field
    name: heightField
    returnTypes:
    - float
  keywords:
  - column
  - cylinder
  - pipe
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
  - label: Infinite Height
    name: Infiniteheight
  - label: Position Along Axis
    name: Createrefaxispos
    summary: 'Create reference to variable: Position Along Axis'
  - label: Normalized Axis Position (0..1)
    name: Createrefnormoffset
    summary: 'Create reference to variable: Normalized Axis Position (0..1)'
  summary: SDF for a cylinder.
  thumb: assets/images/reference/operators/sdf/cylinderSdf_thumb.png

---


SDF for a cylinder.
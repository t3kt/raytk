---
layout: operator
title: torusSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/torusSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.torusSdf/
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
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  keywords:
  - donut
  - ring
  - torus
  name: torusSdf
  opType: raytk.operators.sdf.torusSdf
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Radius
    name: Radius
  - label: Thickness
    name: Thickness
  - label: Translate
    name: Translate
  - label: Enable Caps
    name: Enablecaps
  - label: Start Angle
    name: Startangle
  - label: End Angle
    name: Endangle
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Torus
      name: torus
    name: Uvmode
  - label: Angle (0-360)
    name: Createrefangle
    summary: 'Create reference to variable: Angle (0-360)'
  - label: Normalized Angle (0-1)
    name: Createrefnormangle
    summary: 'Create reference to variable: Normalized Angle (0-1)'
  summary: SDF for a torus.
  thumb: assets/images/reference/operators/sdf/torusSdf_thumb.png

---


SDF for a torus.
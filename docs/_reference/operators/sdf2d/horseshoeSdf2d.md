---
layout: operator
title: horseshoeSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/horseshoeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.horseshoeSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Angle Field
    name: angleField
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
    - vec2
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
    - vec2
    label: Length Field
    name: lengthField
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
    - vec2
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  name: horseshoeSdf2d
  opType: raytk.operators.sdf2d.horseshoeSdf2d
  parameters:
  - label: Angle
    name: Angle
  - label: Radius
    name: Radius
  - label: Length
    name: Length
  - label: Thickness
    name: Thickness
  thumb: assets/images/reference/operators/sdf2d/horseshoeSdf2d_thumb.png

---

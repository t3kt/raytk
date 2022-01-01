---
layout: operator
title: arrowSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/arrowSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.arrowSdf2d/
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
    label: Point Coords Field
    name: points
    returnTypes:
    - vec4
  name: arrowSdf2d
  opType: raytk.operators.sdf2d.arrowSdf2d
  parameters:
  - label: From Point
    name: Pointa
  - label: To Point
    name: Pointb
  - label: Thickness
    name: Thickness
  - label: Head Thickness
    name: Headthickness
  - label: Head Ratio
    name: Headratio
  thumb: assets/images/reference/operators/sdf2d/arrowSdf2d_thumb.png

---

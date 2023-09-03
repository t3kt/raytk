---
layout: operator
title: vesicaSegmentSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/vesicaSegmentSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.vesicaSegmentSdf2d/
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
    label: Point 1 Field
    name: point1
    returnTypes:
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Point 2 Field
    name: point2
    returnTypes:
    - vec4
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
    name: thickness
    returnTypes:
    - float
  name: vesicaSegmentSdf2d
  opType: raytk.operators.sdf2d.vesicaSegmentSdf2d
  parameters:
  - label: Point 1
    name: Pointa
  - label: Point 2
    name: Pointb
  - label: Thickness
    name: Thickness
  thumb: assets/images/reference/operators/sdf2d/vesicaSegmentSdf2d_thumb.png
  variables:
  - label: normoffset
    name: normoffset

---

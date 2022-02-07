---
layout: operator
title: bezierSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/bezierSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.bezierSdf2d/
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
    label: Point A Field
    name: pointA
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
    label: Point B Field
    name: pointB
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
    label: Point C Field
    name: pointC
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  keywords:
  - bezier
  - curve
  - line
  name: bezierSdf2d
  opType: raytk.operators.sdf2d.bezierSdf2d
  parameters:
  - label: Point A
    name: Pointa
  - label: Point B
    name: Pointb
  - label: Point C
    name: Pointc
  - label: Radius
    name: Radius
  status: beta
  thumb: assets/images/reference/operators/sdf2d/bezierSdf2d_thumb.png
  variables:
  - label: normoffset
    name: normoffset

---

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
  name: bezierSdf2d
  opType: raytk.operators.sdf2d.bezierSdf2d
  parameters:
  - label: Point A
    name: Pointa
  - label: Point B
    name: Pointb
  - label: Point C
    name: Pointc
  status: beta
  thumb: assets/images/reference/operators/sdf2d/bezierSdf2d_thumb.png

---

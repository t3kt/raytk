---
layout: operator
title: wedgeSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/wedgeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.wedgeSdf2d/
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
    label: Endpoint 1 Field
    name: endPoint1
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
    label: Endpoint 1 Field
    name: centerPoint
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
    label: Endpoint 2 Field
    name: endPoint2
    returnTypes:
    - vec4
  name: wedgeSdf2d
  opType: raytk.operators.sdf2d.wedgeSdf2d
  parameters:
  - label: End Point 1
    name: Endpoint1
  - label: Center Point
    name: Centerpoint
  - label: End Point 2
    name: Endpoint2
  status: beta
  thumb: assets/images/reference/operators/sdf2d/wedgeSdf2d_thumb.png

---

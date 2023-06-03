---
layout: operator
title: triPlanarCombine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/triPlanarCombine
redirect_from:
  - /reference/opType/raytk.operators.combine.triPlanarCombine/
op:
  category: combine
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
    label: UV Field
    name: uvField
    required: true
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
    - vec3
    label: Normals Field
    name: normalField
    required: true
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
    label: XY Plane
    name: xyField
    returnTypes:
    - float
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
    label: YZ Plane
    name: yzField
    returnTypes:
    - float
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
    label: ZX Plane
    name: zxField
    returnTypes:
    - float
    - vec4
  name: triPlanarCombine
  opType: raytk.operators.combine.triPlanarCombine
  parameters:
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Use Normals
    name: Usenormals
  - label: Blend Mode
    menuOptions:
    - label: Add Axes
      name: add
    - label: Maximum Axes
      name: max
    - label: Average Axes
      name: avg
    name: Blendmode
  - label: Return Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  status: beta

---

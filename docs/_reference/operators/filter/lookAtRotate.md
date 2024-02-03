---
layout: operator
title: lookAtRotate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/lookAtRotate
redirect_from:
  - /reference/opType/raytk.operators.filter.lookAtRotate/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - sourcePointField
    - targetPointField
    - rollField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Source Point Field
    name: sourcePointField
    returnTypes:
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Target Point Field
    name: targetPointField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - sourcePointField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Roll Field
    name: rollField
    returnTypes:
    - float
    supportedVariableInputs:
    - sourcePointField
    - targetPointField
  name: lookAtRotate
  opType: raytk.operators.filter.lookAtRotate
  parameters:
  - label: Enable
    name: Enable
  - label: Source Point
    name: Sourcepoint
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Target Point
    name: Targetpoint
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Roll
    name: Roll
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta

---

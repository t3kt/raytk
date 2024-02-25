---
layout: operator
title: transformSequence
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/transformSequence
redirect_from:
  - /reference/opType/raytk.operators.filter.transformSequence/
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
    - transform1
    - transform2
    - transform3
    - transform4
    - transform5
    - transform6
    supportedVariables:
    - step
    - normstep
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
    label: Transform 1
    name: transform1
    returnTypes:
    - vec4
    supportedVariables:
    - step
    - normstep
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
    label: Transform 2
    name: transform2
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform1
    supportedVariables:
    - step
    - normstep
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
    label: Transform 3
    name: transform3
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-2]
    supportedVariables:
    - step
    - normstep
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
    label: Transform 4
    name: transform4
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-3]
    supportedVariables:
    - step
    - normstep
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
    label: Transform 5
    name: transform5
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-4]
    supportedVariables:
    - step
    - normstep
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
    label: Transform 6
    name: transform6
    returnTypes:
    - vec4
    supportedVariableInputs:
    - transform[1-5]
    supportedVariables:
    - step
    - normstep
  keywords:
  - apply
  name: transformSequence
  opType: raytk.operators.filter.transformSequence
  parameters:
  - label: Enable
    name: Enable
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
    readOnlyHandling: baked
    regularHandling: baked
  - label: Reverse Order
    name: Reverseorder
  - label: Enable Loop
    name: Enableloop
    readOnlyHandling: baked
    regularHandling: baked
  - label: Iterations
    name: Iterations
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  variables:
  - label: step
    name: step
  - label: normstep
    name: normstep

---

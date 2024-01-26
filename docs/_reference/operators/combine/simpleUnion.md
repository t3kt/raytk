---
layout: operator
title: simpleUnion
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/simpleUnion
redirect_from:
  - /reference/opType/raytk.operators.combine.simpleUnion/
op:
  category: combine
  detail: The resulting shape is the combined areas of all of the inputs.
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
    label: SDF 1
    name: definition_in_1
    returnTypes:
    - float
    - Sdf
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
    label: SDF 2
    name: definition_in_2
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp1
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
    label: SDF 3
    name: definition_in_3
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp[1-2]
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
    label: SDF 4
    name: definition_in_4
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp[1-3]
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
    label: SDF 5
    name: definition_in_5
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp[1-4]
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
    label: SDF 6
    name: definition_in_6
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp[1-5]
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
    label: SDF 7
    name: definition_in_7
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp[1-6]
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
    label: SDF 8
    name: definition_in_8
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - inputOp[1-7]
  name: simpleUnion
  opType: raytk.operators.combine.simpleUnion
  parameters:
  - label: Enable
    name: Enable
  shortcuts:
  - su
  summary: Combines several SDFs using the union operator.
  thumb: assets/images/reference/operators/combine/simpleUnion_thumb.png

---


Combines several SDFs using the union operator.

The resulting shape is the combined areas of all of the inputs.
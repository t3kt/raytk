---
layout: operator
title: addFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/addFields
redirect_from:
  - /reference/opType/raytk.operators.combine.addFields/
op:
  category: combine
  detail: If any of the fields is a vector field, all fields will be treated as vector
    fields, with float values copied to each part of the vector.
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
    label: Field 1
    name: definition_in_1
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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Field 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
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
    label: Field 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
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
    label: Field 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
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
    label: Field 5
    name: definition_in_5
    returnTypes:
    - float
    - vec4
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
    label: Field 6
    name: definition_in_6
    returnTypes:
    - float
    - vec4
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
    label: Field 7
    name: definition_in_7
    returnTypes:
    - float
    - vec4
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
    label: Field 8
    name: definition_in_8
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - inputOp[1-7]
  name: addFields
  opType: raytk.operators.combine.addFields
  summary: Adds the values of multiple fields.

---


Adds the values of multiple fields.

If any of the fields is a vector field, all fields will be treated as vector fields, with float values copied to each part of the vector.
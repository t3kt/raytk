---
layout: operator
title: combineFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineFields
redirect_from:
  - /reference/opType/raytk.operators.combine.combineFields/
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
  name: combineFields
  opType: raytk.operators.combine.combineFields
  parameters:
  - label: Enable
    name: Enable
  - label: Operation
    menuOptions:
    - description: Only use the first input (or second depending on `Swaporder`).
      label: 'Off'
      name: 'off'
    - description: Add the fields.
      label: Add
      name: add
    - description: Subtract the second from the first.
      label: Subtract
      name: sub
    - description: Multiply the fields.
      label: Multiply
      name: mul
    - description: Divide the first by the second.
      label: Divide
      name: div
    - description: Average the fields.
      label: Average
      name: avg
    - description: Use the smaller of the field values.
      label: Minimum
      name: min
    - description: Use the larger of the field values.
      label: Maximum
      name: max
    name: Operation
    summary: What operation to use to combine the field values.
  - label: Swap Order
    name: Swaporder
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Swaps the two inputs. This is only relevant for some of the `Operation`
      values.
  - label: Optimize
    name: Optimize
  summary: Combines float or vector fields using one of several mathematical operations.

---


Combines float or vector fields using one of several mathematical operations.
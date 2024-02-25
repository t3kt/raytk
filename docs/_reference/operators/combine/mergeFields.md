---
layout: operator
title: mergeFields
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/mergeFields
redirect_from:
  - /reference/opType/raytk.operators.combine.mergeFields/
op:
  category: combine
  detail: 'This is similar to the Reorder TOP. Each of the 4 vector parts (xyzw) has
    its own source setting specifying which input its value comes from.


    Inputs can either be float fields, or vector fields. If they are vector fields,
    then the corresponding part of that vector is used when creating the output. For
    example, if input 3 is a vector field, and `Source Z` is set to `Input 3`, the
    `z` in the result will be `input1.z`.'
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
  name: mergeFields
  opType: raytk.operators.combine.mergeFields
  parameters:
  - label: Enable
    name: Enable
  - label: X Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcex
    readOnlyHandling: baked
    regularHandling: baked
  - label: Y Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcey
    readOnlyHandling: baked
    regularHandling: baked
  - label: Z Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcez
    readOnlyHandling: baked
    regularHandling: baked
  - label: W Source
    menuOptions:
    - label: Zero
      name: zero
    - label: One
      name: one
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    name: Sourcew
    readOnlyHandling: baked
    regularHandling: baked
  summary: Merges multiple vector fields, using different fields for each vector part.

---


Merges multiple vector fields, using different fields for each vector part.

This is similar to the Reorder TOP. Each of the 4 vector parts (xyzw) has its own source setting specifying which input its value comes from.

Inputs can either be float fields, or vector fields. If they are vector fields, then the corresponding part of that vector is used when creating the output. For example, if input 3 is a vector field, and `Source Z` is set to `Input 3`, the `z` in the result will be `input1.z`.
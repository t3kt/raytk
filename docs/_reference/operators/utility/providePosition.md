---
layout: operator
title: providePosition
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/providePosition
redirect_from:
  - /reference/opType/raytk.operators.utility.providePosition/
op:
  category: utility
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
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
    - Volume
    - Ray
    - Light
    supportedVariables:
    - pos
  name: providePosition
  opType: raytk.operators.utility.providePosition
  variables:
  - label: Position
    name: pos

---

---
layout: operator
title: edgeEngrave
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgeEngrave
redirect_from:
  - /reference/opType/raytk.operators.combine.edgeEngrave/
op:
  category: combine
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius of the groove at different
      points in space, by *multiplying* the value of the `Radius` parameter.
  name: edgeEngrave
  opType: raytk.operators.combine.edgeEngrave
  parameters:
  - label: Enable
    name: Enable
  - label: Swap Inputs
    name: Swapinputs
  - label: Radius
    name: Radius
    summary: Width of the groove.
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Carves a v-shaped groove where the second input intersects with the first.

---

# edgeEngrave

Category: combine



Carves a v-shaped groove where the second input intersects with the first.
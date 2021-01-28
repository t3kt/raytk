---
layout: operator
title: simpleIntersect
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/simpleIntersect
redirect_from:
  - /reference/opType/raytk.operators.combine.simpleIntersect/
op:
  category: combine
  detail: Produces the areas where all input shapes overlap.
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in_3
    name: definition_in_3
    returnTypes:
    - float
    - Sdf
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in_4
    name: definition_in_4
    returnTypes:
    - float
    - Sdf
  name: simpleIntersect
  opType: raytk.operators.combine.simpleIntersect
  parameters:
  - label: Enable
    name: Enable
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Combines SDFs using the intersect operator.

---

# simpleIntersect

Category: combine



Combines SDFs using the intersect operator.

Produces the areas where all input shapes overlap.
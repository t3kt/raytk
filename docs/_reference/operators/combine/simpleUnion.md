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
  name: simpleUnion
  opType: raytk.operators.combine.simpleUnion
  parameters:
  - label: Enable
    name: Enable
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Combines several SDFs using the union operator.

---

# simpleUnion

Category: combine



Combines several SDFs using the union operator.

The resulting shape is the combined areas of all of the inputs.
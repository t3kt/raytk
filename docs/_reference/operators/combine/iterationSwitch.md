---
layout: operator
title: iterationSwitch
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/iterationSwitch
redirect_from:
  - /reference/opType/raytk.operators.combine.iterationSwitch/
op:
  category: combine
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_1
    name: definition_in_1
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: iterationSwitch
  opType: raytk.operators.combine.iterationSwitch
  parameters:
  - label: Enable
    name: Enable
  - label: Scaling
    menuOptions:
    - label: Raw
      name: raw
    - label: Scaled to Total Iterations
      name: scaled
    name: Scaling
  - label: Extend
    menuOptions:
    - label: Clamp
      name: clamp
    - label: Loop
      name: loop
    name: Extend
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help

---

# iterationSwitch

Category: combine


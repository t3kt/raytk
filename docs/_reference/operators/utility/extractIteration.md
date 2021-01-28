---
layout: operator
title: extractIteration
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/extractIteration
redirect_from:
  - /reference/opType/raytk.operators.utility.extractIteration/
op:
  category: utility
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: extractIteration
  opType: raytk.operators.utility.extractIteration
  parameters:
  - label: Enable
    name: Enable
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  status: beta
  summary: 'A field that returns the current iteration, from a downstream

    operator.'

---

# extractIteration

Category: utility



A field that returns the current iteration, from a downstream
operator.
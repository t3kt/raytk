---
layout: operator
title: injectGlobalPosition
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/injectGlobalPosition
redirect_from:
  - /reference/opType/raytk.operators.utility.injectGlobalPosition/
op:
  category: utility
  detail: This can be used for fields that are passed to other ops that are using
    downstream transforms to have the field use the raw global position while being
    used on an op that is transformed.
  inputs:
  - contextTypes:
    - Context
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
    - Ray
    - Light
    - Particle
  name: injectGlobalPosition
  opType: raytk.operators.utility.injectGlobalPosition
  parameters:
  - label: Enable
    name: Enable
  summary: Calls its input using the untransformed global position.

---


Calls its input using the untransformed global position.

This can be used for fields that are passed to other ops that are using downstream transforms to have the field use the raw global position while being used on an op that is transformed.
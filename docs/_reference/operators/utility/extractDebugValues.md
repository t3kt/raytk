---
layout: operator
title: extractDebugValues
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/extractDebugValues
redirect_from:
  - /reference/opType/raytk.operators.utility.extractDebugValues/
op:
  category: utility
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
  name: extractDebugValues
  opType: raytk.operators.utility.extractDebugValues
  parameters:
  - label: Enable
    name: Enable
  status: alpha

---

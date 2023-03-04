---
layout: operator
title: exposeValue
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/exposeValue
redirect_from:
  - /reference/opType/raytk.operators.utility.exposeValue/
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
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
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
    - vec4
    label: Value Field
    name: valueField
    returnTypes:
    - float
    - vec4
  name: exposeValue
  opType: raytk.operators.utility.exposeValue
  parameters:
  - label: Enable
    name: Enable
  - label: Output Buffer
    menuOptions:
    - label: Custom 1
      name: customOut1
    - label: Custom 2
      name: customOut2
    - label: Debug
      name: debugOut
    name: Outputbuffer
  - label: Value Source
    menuOptions:
    - label: Field Value
      name: fieldvalue
    - label: Coordinates
      name: coords
    - label: Iteration
      name: iteration
    name: Valuesource
  - label: Render Stage
    menuOptions:
    - label: Primary
      name: primary
    name: Renderstage
  - label: Only On Surface Hit
    name: Onlyonsurfacehit
  status: beta

---

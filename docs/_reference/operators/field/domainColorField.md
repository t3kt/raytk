---
layout: operator
title: domainColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/domainColorField
redirect_from:
  - /reference/opType/raytk.operators.field.domainColorField/
op:
  category: field
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: domainColorField
  opType: raytk.operators.field.domainColorField
  parameters:
  - label: Enable
    name: Enable
  - label: Grid Spacing
    name: Gridspacing
  - label: Saturation
    name: Saturation
  - label: Grid Strength
    name: Gridstrength
  - label: Mag Strength
    name: Magstrength
  - label: Line Power
    name: Linepower
  status: beta

---

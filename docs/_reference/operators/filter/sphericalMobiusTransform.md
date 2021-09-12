---
layout: operator
title: sphericalMobiusTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/sphericalMobiusTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.sphericalMobiusTransform/
op:
  category: filter
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
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
  name: sphericalMobiusTransform
  opType: raytk.operators.filter.sphericalMobiusTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Center
    name: Center
  - label: Radius
    name: Radius
  - label: Rotate
    name: Rotate
  - label: Rotation Amount
    name: Rotationamount
  status: beta

---

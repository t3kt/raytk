---
layout: operator
title: fold
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/fold
redirect_from:
  - /reference/opType/raytk.operators.filter.fold/
op:
  category: filter
  inputs:
  - contextTypes:
    - none
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
  name: fold
  opType: raytk.operators.filter.fold
  parameters:
  - label: Enable
    name: Enable
  - label: Function
    menuOptions:
    - label: Box Fold
      name: boxfold
    - label: Menger Fold
      name: mengerfold
    name: Function
  - label: Distance
    name: Distance

---

# fold

Category: filter


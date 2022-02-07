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
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
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
  thumb: assets/images/reference/operators/filter/fold_thumb.png

---

---
layout: operator
title: moduloDistance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloDistance
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloDistance/
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
    - VertexContext
    - PixelContext
    coordTypes:
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
    - Particle
    supportedVariables:
    - RTK_raytk_operators_filter_moduloDistance_ring
  keywords:
  - distance
  - modulo
  - polar
  - radial
  - repeat
  name: moduloDistance
  opType: raytk.operators.filter.moduloDistance
  parameters:
  - label: Enable
    name: Enable
  - label: Distance Mode
    menuOptions:
    - label: X Axis
      name: xaxis
    - label: Y Axis
      name: yaxis
    - label: Z Axis
      name: zaxis
    - label: Spherical
      name: spherical
    name: Distancemode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Length
    name: Length
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Iterate On Rings
    name: Iterateonrings
    readOnlyHandling: semibaked
    regularHandling: semibaked
  variables:
  - label: RTK_raytk_operators_filter_moduloDistance_ring
    name: RTK_raytk_operators_filter_moduloDistance_ring

---

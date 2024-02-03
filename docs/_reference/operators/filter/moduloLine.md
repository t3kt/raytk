---
layout: operator
title: moduloLine
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloLine
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloLine/
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
    supportedVariables:
    - cellcoord
    - normcoord
  name: moduloLine
  opType: raytk.operators.filter.moduloLine
  parameters:
  - label: Enable
    name: Enable
  - label: Point 1
    name: Point1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Divisions
    name: Divisions
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Mirror Type
    menuOptions:
    - label: None
      name: none
    - label: Mirror
      name: mirror
    name: Mirrortype
    summary: How to the slices are varied.
  status: beta
  variables:
  - label: cellcoord
    name: cellcoord
  - label: normcoord
    name: normcoord

---

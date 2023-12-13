---
layout: operator
title: circularRepeat
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/circularRepeat
redirect_from:
  - /reference/opType/raytk.operators.filter.circularRepeat/
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
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: circularRepeat
  opType: raytk.operators.filter.circularRepeat
  parameters:
  - label: Enable
    name: Enable
  - label: Plane
    menuOptions:
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    name: Plane
  - label: Radius
    name: Radius
    summary: Size of the area to fill.
  - label: Cell Size
    name: Cellsize
    summary: Spacing between copies.
  status: beta
  summary: Repeat an SDF to fill a 2D circular area.
  variables:
  - label: cellcoord
    name: cellcoord
  - label: cellchecker
    name: cellchecker

---


Repeat an SDF to fill a 2D circular area.
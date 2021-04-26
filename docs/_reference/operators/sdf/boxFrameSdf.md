---
layout: operator
title: boxFrameSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/boxFrameSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.boxFrameSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scale_definition_in
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thickness_definition_in
    returnTypes:
    - float
  name: boxFrameSdf
  opType: raytk.operators.sdf.boxFrameSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Move the center of the shape.
  - label: Scale
    name: Scale
    summary: The size of the box.
  - label: Thickness
    name: Thickness
    summary: The thickness of the bars of the box.
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  summary: SDF for the squared frame of the edges of a box.

---


SDF for the squared frame of the edges of a box.
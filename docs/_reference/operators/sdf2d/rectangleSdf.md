---
layout: operator
title: rectangleSdf
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/rectangleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.rectangleSdf/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
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
    - vec2
    label: Translate Field
    name: translate_definition_in
    returnTypes:
    - float
    - vec4
  name: rectangleSdf
  opType: raytk.operators.sdf2d.rectangleSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the rectangle.
  - label: Scale
    name: Scale
    summary: The size of the rectangle on the x and y axes.
  summary: SDF for a 2D rectangle.

---


SDF for a 2D rectangle.
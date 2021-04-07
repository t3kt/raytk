---
layout: operator
title: pyramidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/pyramidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.pyramidSdf/
op:
  category: sdf
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
    label: Height Field
    name: height_field_definition_in
    returnTypes:
    - float
    summary: Optional field used to determine the height. When connected, the `Height`
      is multiplied by the value produced by the field.
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
    label: Width Field
    name: width_field_definition_in
    returnTypes:
    - float
    summary: Optional field used to determine the width. When connected, the `Width`
      is multiplied by the value produced by the field.
  name: pyramidSdf
  opType: raytk.operators.sdf.pyramidSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the base of the pyramid.
  - label: Height
    name: Height
    summary: The height of the pyramid.
  - label: Width
    name: Width
    summary: The width of the base of the pyramid. Note that widths smaller than 0.5
      will produce rendering errors.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  summary: A pyramid with four sides.

---


A pyramid with four sides.
---
layout: operator
title: uvField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/uvField
redirect_from:
  - /reference/opType/raytk.operators.field.uvField/
op:
  category: field
  detail: 'This can be used within modular materials for texture lookups.


    For surfaces that have assigned UV coordinates, the W part of the produced vector
    will be 1. For surfaces without UV coordinates, all parts of the vector will be
    0.'
  name: uvField
  opType: raytk.operators.field.uvField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  summary: Field that produces surface UV coordinates, if available.
  thumb: assets/images/reference/operators/field/uvField_thumb.png

---


Field that produces surface UV coordinates, if available.

This can be used within modular materials for texture lookups.

For surfaces that have assigned UV coordinates, the W part of the produced vector will be 1. For surfaces without UV coordinates, all parts of the vector will be 0.
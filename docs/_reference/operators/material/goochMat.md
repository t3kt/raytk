---
layout: operator
title: goochMat
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/goochMat
redirect_from:
  - /reference/opType/raytk.operators.material.goochMat/
op:
  category: material
  detail: 'It produces colors that are based on the surface normal. It is useful for
    showing the 3D structure of a shape rather than using realistic lighting-based
    color.


    See [Gooch Shading](https://en.wikipedia.org/wiki/Gooch_shading).


    This is equivalent to the `goochShadingContrib` packaged as a self-contained material.'
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
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
  name: goochMat
  opType: raytk.operators.material.goochMat
  parameters:
  - label: Enable
    name: Enable
  - label: Base Color
    name: Basecolor
  - label: Warm Color
    name: Warmcolor
  - label: Cool Color
    name: Coolcolor
  status: beta
  summary: A material that uses the Gooch shading model.

---


A material that uses the Gooch shading model.

It produces colors that are based on the surface normal. It is useful for showing the 3D structure of a shape rather than using realistic lighting-based color.

See [Gooch Shading](https://en.wikipedia.org/wiki/Gooch_shading).

This is equivalent to the `goochShadingContrib` packaged as a self-contained material.
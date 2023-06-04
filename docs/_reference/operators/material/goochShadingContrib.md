---
layout: operator
title: goochShadingContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/goochShadingContrib
redirect_from:
  - /reference/opType/raytk.operators.material.goochShadingContrib/
op:
  category: material
  detail: 'It produces colors that are based on the surface normal. It is useful for
    showing the 3D structure of a shape rather than using realistic lighting-based
    color.


    See [Gooch Shading](https://en.wikipedia.org/wiki/Gooch_shading).


    This is equivalent to the `goochMat`, for use in a modular material.'
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Base Color Field
    name: baseColorField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Warm Color Field
    name: warmColorField
    returnTypes:
    - float
    - vec4
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Cool Color Field
    name: coolColorField
    returnTypes:
    - float
    - vec4
  name: goochShadingContrib
  opType: raytk.operators.material.goochShadingContrib
  parameters:
  - label: Level
    name: Level
  - label: Use Light Color
    name: Uselightcolor
  - label: Enable Shadow
    name: Enableshadow
  - label: Base Color
    name: Basecolor
  - label: Warm Color
    name: Warmcolor
  - label: Cool Color
    name: Coolcolor
  - label: Enable
    name: Enable
  summary: A material element that uses the Gooch shading model.

---


A material element that uses the Gooch shading model.

It produces colors that are based on the surface normal. It is useful for showing the 3D structure of a shape rather than using realistic lighting-based color.

See [Gooch Shading](https://en.wikipedia.org/wiki/Gooch_shading).

This is equivalent to the `goochMat`, for use in a modular material.
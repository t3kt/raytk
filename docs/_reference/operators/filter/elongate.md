---
layout: operator
title: elongate
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/elongate
redirect_from:
  - /reference/opType/raytk.operators.filter.elongate/
op:
  category: filter
  detail: 'For example, a capsule is an elongated version of a sphere.


    It is based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm)
    from Inigo Quilez.

    See [example](https://www.shadertoy.com/view/Ml3fWj).'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
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
  name: elongate
  opType: raytk.operators.filter.elongate
  parameters:
  - label: Enable
    name: Enable
  - label: Center
    name: Center
    summary: The center point of the stretching.
  - label: Size
    name: Size
    summary: The distance that that parts are pushed apart from the origin.
  summary: Stretches a shape by splitting it into pieces, moves them apart, and connects
    them.

---


Stretches a shape by splitting it into pieces, moves them apart, and connects them.

For example, a capsule is an elongated version of a sphere.

It is based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Ml3fWj).
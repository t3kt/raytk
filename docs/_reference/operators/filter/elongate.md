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

    See [example](https://www.shadertoy.com/view/Ml3fWj).


    * `Enable` - Enables or disables the op.

    * `Size` - The distance that that parts are pushed apart from the origin.'
  inputs:
  - contextTypes:
    - none
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
  - label: Size
    name: Size
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Splits a shape into pieces, moves them apart, and connects them.

---

# elongate

Category: filter



Splits a shape into pieces, moves them apart, and connects them.

For example, a capsule is an elongated version of a sphere.

It is based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Ml3fWj).

* `Enable` - Enables or disables the op.
* `Size` - The distance that that parts are pushed apart from the origin.
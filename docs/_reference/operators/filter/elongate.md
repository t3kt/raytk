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
    - ParticleContext
    - VertexContext
    - PixelContext
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
    - Particle
    supportedVariableInputs:
    - sizeField
    - centerField
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
    - vec2
    - vec3
    label: Size Field
    name: sizeField
    returnTypes:
    - vec4
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
    - vec2
    - vec3
    label: Center Field
    name: centerField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - sizeField
  keywords:
  - elongate
  - extend
  - stretch
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
  - label: Axes
    menuOptions:
    - label: XYZ
      name: xyz
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: XZ
      name: xz
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axes
  summary: Stretches a shape by splitting it into pieces, moves them apart, and connects
    them.
  thumb: assets/images/reference/operators/filter/elongate_thumb.png

---


Stretches a shape by splitting it into pieces, moves them apart, and connects them.

For example, a capsule is an elongated version of a sphere.

It is based on [code](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm) from Inigo Quilez.
See [example](https://www.shadertoy.com/view/Ml3fWj).